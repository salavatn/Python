from s3.s3buckets import S3Buckets
from s3.config.settings import table_buckets, table_files, console
from s3.config.settings import s3_parser
from s3.config.settings import logger 
from rich import print

from rich.tree import Tree


# logger = logger.getLogger(__name__)
logger = logger.getLogger('Console:Client')



class S3Client:
    def __init__(self):
        self.s3_buckets = S3Buckets()

    def s3_bucket_list(self) -> dict:
        '''List all buckets in S3'''

        # Part 0: Prepare variables and constants
        log_header   = 'S3:List:'
        all_buckets  = self.s3_buckets.list_buckets()
        bucket_count = 0
        row          = ["*", "*", "*", "*", "*"]

        # Part 1: Check if the job finished with error
        if all_buckets is False:
            logger.debug(f'{log_header} Job finished with error')
            return False

        # Part 2: Check if there are no buckets        
        if len(all_buckets) == 0:
            logger.debug(f'{log_header} no buckets found;')
            table_buckets.add_row(*row)
            console.print(table_buckets)
            return True
        
        # Part 3: Print the table with all buckets
        for one_bucket in all_buckets:
            bucket_count  += 1
            row_bucket     = [
                str(bucket_count),          # ID for table
                one_bucket['content'],      # count of files
                one_bucket['bucket'],       # bucket name
                one_bucket['location'],     # bucket region
                one_bucket['created'] ]     # bucket created
            table_buckets.add_row(*row_bucket)
            logger.debug(f'{log_header} found bucket {one_bucket["bucket"]};')
        console.print(table_buckets)
        return True

    def s3_delete_bucket(self, bucket_name, force):
        '''IN-PROGRESS: Delete bucket'''
        log_header = 'Deleting:'

        result = self.s3_buckets.delete_bucket(bucket_name, force)

        if result:
            logger.info(f'{log_header} The deletion of bucket "{bucket_name}" was successful;')
        else:
            logger.error(f'{log_header} The job finished with error;')


    def s3_delete_dir(self, bucket_name, directory):
        '''IN-PROGRESS: Delete bucket'''
        log_header = 'Deleting:'

        result = self.s3_buckets.delete_folder(bucket_name, directory)


    def s3_bucket_content(self, bucket_name):
        data = self.s3_buckets.content_bucket(bucket_name)

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

    def s3_bucket_create(self, bucket_name):
        log_header = 'Creating:'
        result = self.s3_buckets.create_bucket(bucket_name)
        if result:
            logger.debug(f'{log_header} new bucket {bucket_name} is created;')
        else:
            logger.debug(f'{log_header} bucket {bucket_name} is not created;')

    def s3_bucket_upload(self, bucket_name, file_path):
        # file_name = 'my_pdf_document.pdf'
        self.s3_buckets.upload_file(bucket_name, file_path)

