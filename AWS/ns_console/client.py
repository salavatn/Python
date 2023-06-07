from ns_aws.s3buckets import S3Buckets
from ns_config.settings import table_buckets, table_files, console
from ns_config.settings import s3_parser, aws_region
from ns_config.settings import logger
from rich import print

from rich.tree import Tree

s3_buckets = S3Buckets()

# logger = logger.getLogger(__name__)
logger = logger.getLogger('NS_CONSOLE:Client')

import math

def convert_bytes(size_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    index = int(math.floor(math.log(size_bytes, 1024)))
    size = round(size_bytes / (1024 ** index), 2)
    unit = units[index]
    return size, unit


def s3_bucket_list() -> None:
    all_buckets = s3_buckets.list_buckets()
    # print(buckets)
    
    for one_bucket in all_buckets:
        count   = str(one_bucket['count'])
        bucket  = one_bucket['bucket']
        created = str(one_bucket['created'])
        region  = one_bucket['location'].upper()
        
        row = [count, bucket, region, created]
        table_buckets.add_row(*row)

    console.print(table_buckets)


def s3_bucket_delete(bucket_name):
    '''IN-PROGRESS: Delete bucket'''
    s3_buckets.delete_bucket(bucket_name)
    # logger.info(f'Bucket {bucket_name} deleted')

    try:
        # Attempt to delete the bucket
        response = s3_buckets.delete_bucket(Bucket=bucket_name)
        print('Bucket deleted successfully.')
    except Exception as error:
        logger.error(f'Bucket error: {error}')

        # Catch the specific exception
        if "BucketNotEmpty" in error:
            # Force delete the bucket
            try:
                bucket_objects = s3_buckets.list_objects_v2(Bucket=bucket_name)['Contents']
                bucket_objects = [{'Key': obj['Key']} for obj in bucket_objects]
                s3_buckets.delete_objects(Bucket=bucket_name, Delete={'Objects': bucket_objects})
                s3_buckets.delete_bucket(Bucket=bucket_name)
                print('Bucket forcefully deleted.')
            except Exception as error:
                print('Error:', error)
        else:
            print('An error occurred:', error)


def s3_bucket_content(bucket_name):
    data = s3_buckets.check_bucket(bucket_name)
    logger.info(f'Bucket {bucket_name} checked')

    count = 0
    for path in data:
        

        # Ignore hidden files
        if '/.' in path['Key']:
            continue
        
        count += 1


        # Field-1,2: Path and File
        full_path = path['Key']
        file_name = full_path.split('/')[-1]
        full_path = full_path.replace(file_name, '')

        # Field-3: Extension
        extension = file_name.split('.')[-1]
        extension = extension.upper()

        # Field-3: Created Date and Time
        created = path['LastModified']
        created = created.strftime("%Y-%m-%d %H:%M:%S")


        # Field-4: Size
        size = path['Size']
        size, unit = convert_bytes(size)
        file_size = f'{size} {unit}'
        # logger.info(f'{full_path}, {file_name}, {created}, {size} {unit}')

        row = [str(count), full_path, file_name, extension, file_size, created]
        table_files.add_row(*row)
    console.print(table_files)


def s3_bucket_create(bucket_name):
    s3_buckets.create_bucket(bucket_name, aws_region)
    logger.info(f'Bucket {bucket_name} created')








args = s3_parser.parse_args()
s3_list = args.list
s3_create = args.create
s3_delete = args.delete
s3_bucket = args.bucket
s3_verbose = args.verbose
s3_force = args.force
s3_content= args.content

if s3_list:    
    s3_bucket_list()

if s3_delete:
    s3_bucket_delete(s3_bucket)

if s3_content:
    s3_bucket_content(s3_bucket)

if s3_create:
    s3_bucket_create(s3_bucket)









# webapp2-dev-serverlessdeploymentbucket-j4yn3xoell07