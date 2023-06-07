from ns_config.settings import aws_session, aws_region
from ns_config.settings import logger
from ns_config.libraries import List, Union, Dict, Any
# from botocore.exceptions import ClientError

# from datetime import datetime
from rich import print
# from rich.tree import Tree
# import os

from ns_converter.converter import convert_bytes


import threading
logger = logger.getLogger('NS_AWS:S3Buckets')


class S3Buckets:
    def __init__(self):
        self.s3_client = aws_session.client('s3')

    def list_buckets(self) -> Union[List, False]:
        '''List all buckets in S3'''
        log_header  = 'ListBuckets:'
        backets_all = self.s3_client.list_buckets()
        status_code = backets_all['ResponseMetadata']['HTTPStatusCode']

        if status_code != 200:
            logger.error(f'{log_header} status_code is {status_code};')
            raise Exception(f'{log_header} Connection to AWS with status_code {status_code};')

        self.bucket_list = []
        thread_list = []

        for bucket in backets_all['Buckets']:
            thread = threading.Thread(target=self.process_bucket, args=(bucket,))
            thread.start()
            thread_list.append(thread)
        for thread in thread_list:
            thread.join()

        return self.bucket_list
    


    def process_bucket(self, bucket):
        log_header  = 'ProcessBucket:'        
        bucket_name = bucket['Name']
        content     = self.content_bucket(bucket_name)
        if content is None or content is False:
            content = 0
        else:
            content  = len(content)
        created_date = bucket['CreationDate'].strftime('%Y-%m-%d %H:%M:%S')
        try:
            response      = self.s3_client.get_bucket_location(Bucket=bucket_name)
            bucket_region = response['LocationConstraint']
        except Exception as error:

            msg_err = str(error)

            if "(NoSuchBucket)" in msg_err:
                logger.error(f'{log_header} Bucket "{bucket_name}" not found or deleted;')
                bucket_region = '-- Not found --'
                return
            logger.error(f'{log_header} error: {error}')
            
        if bucket_region is None:
            bucket_region = 'us-east-1'

        bucket_dict = {
            'bucket':   str(bucket_name),
            'created':  str(created_date),
            'location': str(bucket_region).upper(),
            'content':  str(content)
        }
        self.bucket_list.append(bucket_dict)





    def create_bucket(self, bucket_name):
        '''Create bucket'''
        log_header = 'Creating:'

        # Part-1: Check-1: If bucket_name is None, return False
        if bucket_name is None:
            logger.error(f'{log_header} bucket_name is None;')
            logger.warning(f'{log_header} Please provide bucket_name. Use -b "bucket-name" option.')
            return False
        
        # Part-2: Prepare data - bucket_name and region
        data = {
            'Bucket': bucket_name,
            'CreateBucketConfiguration': {
                'LocationConstraint': aws_region
                }
            }
        
        # Part-3: Create bucket
        try:
            response = self.s3_client.create_bucket(**data)
        except Exception as error:
            msg_err = str(error)
            # print(msg_err)
            if '(BucketAlreadyOwnedByYou)'in msg_err:
                logger.info(f'{log_header} Bucket "{bucket_name}" already exists;')
                return True
            elif '(InvalidBucketName)' in msg_err:
                logger.error(f'{log_header} Bucket name "{bucket_name}" is not valid;')
                logger.warning(f'{log_header} Allowed characters are a-z, ".", "-", 0-9;')
                return False

            msg = str(error.response['Error']['Message'])
            logger.error(f'{log_header} {msg}')

            return False
        
        status_code = response['ResponseMetadata']['HTTPStatusCode']

        # Part-4: Check-2: If status_code is not 200, return False
        if status_code != 200:
            logger.error(f'{log_header} status_code is {status_code};')
            return False
        
        # Part-5: Check-3: If status_code is 200, return True
        
        logger.info(f'{log_header} Bucket "{bucket_name}" created;')
        return True



    def delete_bucket(self, bucket_name, force):
        '''Delete bucket'''
        log_header = 'Delete:'

        if force:
            try:
                full_objects = self.s3_client.list_objects_v2(Bucket=bucket_name)['Contents']
                list_objects = [{'Key': obj['Key']} for obj in full_objects]
                self.s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': list_objects})
            except Exception as error:
                msg = error.response['Error']['Message']
                logger.error(f'{log_header} {msg}')
                return False
                
        try:
            self.s3_client.delete_bucket(Bucket=bucket_name)
        except Exception as error:
            msg = error.response['Error']['Message']
            logger.error(f'{log_header} {msg}')

            err_msg = str(error)
            if "(BucketNotEmpty)" in err_msg:
                logger.warning(f'{log_header} Check contents of bucket. Use --content option.')
                logger.warning(f'{log_header} If you want to delete bucket forcefully, use --force option.')

            return False
        
        
        logger.info(f'{log_header} Bucket {bucket_name} deleted successfully.')


    def content_bucket(self, bucket_name):
        '''Content bucket'''
        log_header = 'ContentBucket:'

        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        except Exception as error:
            msg_err = str(error)
            msg = error.response['Error']['Message']
            logger.error(f'{log_header} {msg}')
            return False


        if 'Contents' not in response:
            logger.warning(f'{log_header} Bucket "{bucket_name}" is empty;')
            return None
        
        
        data = response['Contents']
        list_files = []


        count = 0
        for path in data:
            
            # Part-1: Skip if folder is hidden (.git, .vscode, etc.)
            if '/.' in path['Key']:
                continue
            
            count += 1
            id = str(count)

            # Part-2: Get File name and Full Path
            full_path = path['Key']
            file_name = full_path.split('/')[-1]
            full_path = full_path.replace(file_name, '')

            # Part-3: Get File Extension
            extension = file_name.split('.')[-1]
            extension = extension.upper()

            # Part-4: Get Date Created
            created = path['LastModified']
            created = created.strftime("%Y-%m-%d %H:%M:%S")

            # Part-5: Get File Size
            size = path['Size']
            size, unit = convert_bytes(size)
            file_size = f'{size} {unit}'

            file_info = [id, full_path, file_name, extension, file_size, created]
            # print(file_info)

            list_files.append(file_info)


        return list_files
