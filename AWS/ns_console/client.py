from ns_aws.s3buckets import S3Buckets
from ns_config.settings import table_buckets, table_files, console
from ns_config.settings import s3_parser
from ns_config.settings import logger
from rich import print

from rich.tree import Tree

s3_buckets = S3Buckets()

# logger = logger.getLogger(__name__)
logger = logger.getLogger('NS_CONSOLE:Client')
import time



def s3_bucket_list() -> None:
    '''List all buckets in S3'''

    start_time = time.time()
    all_buckets = s3_buckets.list_buckets()
    finish_time = time.time()
    elapsed_time = finish_time - start_time

    print(f'Elapsed time: {elapsed_time}!')

    if len(all_buckets) == 0:
        print('No buckets found')
        return

    count = 0
    for one_bucket in all_buckets:
        count   += 1
        bucket  = one_bucket['bucket']
        created = one_bucket['created']
        region  = one_bucket['location']
        content = one_bucket['content']
        
        row = [str(count), content, bucket, region, created]
        table_buckets.add_row(*row)

    console.print(table_buckets)


def s3_bucket_delete(bucket_name, force):
    '''IN-PROGRESS: Delete bucket'''
    s3_buckets.delete_bucket(bucket_name, force)


def s3_bucket_content(bucket_name):
    data = s3_buckets.content_bucket(bucket_name)

    if data is False:
        logger.error(f'Bucket {bucket_name} not found')
        return
    
    if data is None:
        logger.info(f'Bucket {bucket_name} is empty')
        table_files.add_row('*', '*', '*', '*', '*', '*')
        console.print(table_files)
        return

    for file in data:
        table_files.add_row(*file)
    console.print(table_files)


def s3_bucket_create(bucket_name):
    s3_buckets.create_bucket(bucket_name)



args        = s3_parser.parse_args()
s3_list     = args.list
s3_create   = args.create
s3_delete   = args.delete
s3_bucket   = args.bucket
s3_force    = args.force
s3_content  = args.content


if s3_list:    
    s3_bucket_list()

if s3_delete:
    s3_bucket_delete(s3_bucket, s3_force)

if s3_content:
    s3_bucket_content(s3_bucket)

if s3_create:
    s3_bucket_create(s3_bucket)









# webapp2-dev-serverlessdeploymentbucket-j4yn3xoell07