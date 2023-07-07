from s3.console.client import S3Client 
from s3.config.settings import logger, s3_parser 


# Section 1: Create instance of S3Client
s3_client = S3Client()


# Section 2: Parse arguments
args        = s3_parser.parse_args()
# s3_list     = args.list
s3_create   = args.create
# s3_delete   = args.delete
s3_bucket   = args.bucket
s3_force    = args.force
s3_content  = args.content
s3_file     = args.file
s3_dir      = args.dir


# Parse the command-line arguments
args = s3_parser.parse_args()


# Section 3: Run the job
if args.list:   s3_client.s3_bucket_list()


if args.delete and not args.dir:
    # s3_parser.error("\nPlease provide a name of Dir or File to delete")
    s3_parser.print_help()
elif args.delete and args.dir:
    s3_client.s3_delete_dir(s3_bucket, s3_dir)


# if s3_delete and s3_dir:
#     print("Delete dir")
#     s3_client.s3_delete_dir(s3_bucket, s3_dir)


# if s3_delete:
#     print("Delete bucket")
    
#     s3_client.s3_delete_bucket(s3_bucket, s3_force)

if s3_content:
    s3_client.s3_bucket_content(s3_bucket)

if s3_create:
    s3_client.s3_bucket_create(s3_bucket)

if s3_file:
    s3_client.s3_bucket_upload(s3_bucket, s3_file)





