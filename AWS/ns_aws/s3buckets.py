from ns_config.settings import aws_session
from ns_config.settings import logger
from ns_config.libraries import List
# from botocore.exceptions import ClientError

from datetime import datetime
from rich import print
from rich.tree import Tree
import os



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




    def delete_bucket(self, bucket_name):
        '''Delete bucket'''
        log_header = 'Delete:'
        try:
            self.s3_client.delete_bucket(Bucket=bucket_name)
        except Exception as error:
            logger.error(f'{log_header} {error}')
            return False
    
    def check_bucket(self, bucket_name):
        '''Check bucket'''
        log_header = 'CheckBucket:'
        # try:
        #     test = self.s3_client.head_bucket(Bucket=bucket_name)
        #     for key, value in test.items():
        #         print(f'{key}: {value}')
        # except Exception as error:
        #     logger.error(f'{log_header} {error}')
        #     return False
        # return True





        # List all objects in the bucket
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        # print(f'Objects in bucket: {response}')
        data = response['Contents']
        # print(f'Objects in bucket: {data}')
        return data
        # for element in response['Contents']:
        #     print(f'Element: {element}')



        


        # # Print the object names
        # if 'Contents' in response:
            
        #     for obj in response['Contents']:
        #         print(obj['Key'])
        # else:
        #     print('No objects found in the bucket.')


