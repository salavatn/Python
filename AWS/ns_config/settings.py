from ns_config.libraries import load_dotenv
from ns_config.libraries import os
from ns_config.libraries import boto3
from ns_config.libraries import logging, logging_config, colorlog
from ns_config.libraries import Console, Table, box
from ns_config.libraries import argparse

# from ns_config.libraries import Console, Table, box
# from ns_config.libraries import pytz, datetime
# from ns_config.libraries import Faker


# Setting-1: Load environment variables
load_env = load_dotenv(dotenv_path='ns_config/.env')


# Setting-2: Load AWS credentials and create AWS Session
aws_access  = os.getenv('PYTHON_AWS_KEY')
aws_secret  = os.getenv('PYTHON_AWS_SECRET')
aws_region  = os.getenv('PYTHON_AWS_REGION')
aws_params  = {
    'aws_access_key_id':     aws_access,
    'aws_secret_access_key': aws_secret,
    'region_name':           aws_region
}
aws_session = boto3.Session(**aws_params)


# Setting-3: Logging
logging_config.fileConfig('ns_config/logging.conf')
logger = logging


# Setting-4: Tables
console = Console()
#           Table-4.1: Show list of buckets
table_buckets = Table(title='\nAWS S3 Buckets', show_header=True, header_style="bold magenta", box=box.SIMPLE)
table_buckets.add_column("ID", style="dim", justify="center")
table_buckets.add_column("Bucket")
table_buckets.add_column("Location", justify="left")
table_buckets.add_column("Created", justify="center")

#           Table-4.2: Show list of files in a bucket
table_files = Table(title='\nFiles in AWS S3 Bucket', show_header=True, header_style="bold magenta", box=box.SIMPLE)
table_files.add_column("ID", style="dim", justify="center", width=4)
table_files.add_column("Path", style="dim")
table_files.add_column("File", justify="left")
table_files.add_column("Extension", justify="left")
table_files.add_column("Size", justify="right")
table_files.add_column("Created", justify="center")


# Setting-5: ArgParse
s3_parser = argparse.ArgumentParser(description='AWS S3 Buckets')
s3_parser.add_argument('--list', action='store_true', help='List all buckets')
s3_parser.add_argument('--create', action='store_true', help='Create bucket')
s3_parser.add_argument('--delete', action='store_true', help='Delete bucket')
s3_parser.add_argument('--content', action='store_true', help='Test mode')
s3_parser.add_argument('-b', '--bucket', type=str, help='Bucket name')
s3_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
s3_parser.add_argument('-f', '--force', action='store_true', help='Force mode')
