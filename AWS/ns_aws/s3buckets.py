from ns_config.settings import aws_session
from ns_config.settings import logger
from ns_config.libraries import List
# from botocore.exceptions import ClientError

from datetime import datetime
from rich import print
from rich.tree import Tree
import os

from ns_converter.converter import convert_bytes



logger = logger.getLogger('NS_AWS:S3Buckets')


class S3Buckets:
    def __init__(self):
        self.s3_client = aws_session.client('s3')

    def list_buckets(self) -> List:
        '''List all buckets in S3'''
        log_header   = 'ListBuckets:'

        # Part-1: List all buckets and get status code
        backets_all  = self.s3_client.list_buckets()
        status_code  = backets_all['ResponseMetadata']['HTTPStatusCode']


        # Part-2: Check status code
        if status_code != 200:
            logger.error(f'{log_header} status_code is {status_code};')
            return False

        # Part-3: Create list of buckets
        buckets_list = []
        count = 0
        for bucket in backets_all['Buckets']:
            count += 1
            bucket_name = bucket['Name']
            created = bucket['CreationDate']
            created = created.strftime('%Y-%m-%d %H:%M:%S')

            response = self.s3_client.get_bucket_location(Bucket=bucket_name)
            # print(response)
            bucket_location = response['LocationConstraint']

            if bucket_location is None:
                bucket_location = 'us-east-1'
            # print(bucket_location)

            bucket_dict = {
                'count': count,
                'bucket': bucket_name,
                'created': created,
                'location': bucket_location
                }
            # print(bucket_dict)
            buckets_list.append(bucket_dict)
        

        

        return buckets_list

    def create_bucket(self, bucket_name, region_name):
        response = self.s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region_name
            }
        )
        logger.info(f'Bucket {bucket_name} created successfully.')

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
        '''Check bucket'''
        log_header = 'CheckBucket:'

        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
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
