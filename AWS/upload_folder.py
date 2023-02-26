# RUN: upload_folder.py /path/to/local/folder theBucketName /path/to/s3/folder
import os
import sys
import boto3

local_directory, bucket, destination = sys.argv[1:4]

client = boto3.client('s3')

for root, dirs, files in os.walk(local_directory):

  for filename in files:
    local_path = os.path.join(root, filename)
    relative_path = os.path.relpath(local_path, local_directory)
    s3_path = os.path.join(destination, relative_path)
    print('Searching "%s" in "%s"' % (s3_path, bucket))
    try:
        client.head_object(Bucket=bucket, Key=s3_path)
        print("Path found on S3! Skipping %s..." % s3_path)
    except:
        print("Uploading %s..." % s3_path)
        client.upload_file(local_path, bucket, s3_path)
