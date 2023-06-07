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

    all_buckets  = s3_buckets.list_buckets()
    bucket_count = 0

    if all_buckets is False:
        logger.debug('Job finished with error')
        return
    
    if len(all_buckets) == 0:
        print('No buckets found')
        return

    for one_bucket in all_buckets:
        bucket_count  += 1
        bucket_name    = one_bucket['bucket']
        backet_created = one_bucket['created']
        bucket_region  = one_bucket['location']
        content_count  = one_bucket['content']
        
        row = [
            str(bucket_count), 
            content_count, 
            bucket_name, 
            bucket_region, 
            backet_created
            ]
        table_buckets.add_row(*row)

    console.print(table_buckets)

def s3_bucket_delete(bucket_name, force):
    '''IN-PROGRESS: Delete bucket'''
    log_header = 'Deleting:'

    result = s3_buckets.delete_bucket(bucket_name, force)

    if result:
        logger.info(f'{log_header} The deletion of bucket "{bucket_name}" was successful;')
    else:
        logger.error(f'{log_header} The job finished with error;')

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

def s3_bucket_upload(bucket_name, file_path):
    # file_name = 'my_pdf_document.pdf'
    s3_buckets.upload_file(bucket_name, file_path)


args        = s3_parser.parse_args()
s3_list     = args.list
s3_create   = args.create
s3_delete   = args.delete
s3_bucket   = args.bucket
s3_force    = args.force
s3_content  = args.content
s3_file     = args.file

if s3_list:    
    s3_bucket_list()

if s3_delete:
    s3_bucket_delete(s3_bucket, s3_force)

if s3_content:
    s3_bucket_content(s3_bucket)

if s3_create:
    s3_bucket_create(s3_bucket)


if s3_file:
    print('File:', s3_file)
    print('Bucket:', s3_bucket)
    print('Force:', s3_force)
    s3_bucket_upload(s3_bucket, s3_file)








# webapp2-dev-serverlessdeploymentbucket-j4yn3xoell07