import json
from datetime import datetime

my_text = "{'ResponseMetadata': {'RequestId': '637G67FC25716K7S', 'HostId': 'LLPt+098kRy8LvDKmJvt0OnVcnOjq2Qi71bfq4AeH4+yJafUnMXiC8SU3mzT5C0yzTZNBwBIvxw=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'LLPt+098kRy8LvDKmJvt0OnVcnOjq2Qi71bfq4AeH4+yJafUnMXiC8SU3mzT5C0yzTZNBwBIvxw=', 'x-amz-request-id': '637G67FC25716K7S', 'date': 'Tue, 14 Feb 2023 12:44:40 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'ns-lab-web', 'CreationDate': datetime.datetime(2022, 12, 3, 8, 3, 52, tzinfo=tzlocal())}, {'Name': 'ns-lab.open-storage', 'CreationDate': datetime.datetime(2023, 2, 14, 8, 45, 55, tzinfo=tzlocal())}], 'Owner': {'DisplayName': 'salavat', 'ID': 'a832a8b8a4e6cf3a0ca798daa02b087110234b6db836b61904789188f9615fb0'}}"
my_text = my_text.replace(', tzinfo=tzlocal()', '')

index = my_text.find("datetime.datetime")

while index >= 1:
    my_date_time = my_text[index:index+40]      # datetime.datetime(2022, 12, 3, 8, 3, 52)
    my_text = my_text.replace(my_date_time, f"'{my_date_time[17:]}'")
    index = my_text.find("datetime.datetime")
    print(my_text)





# date_time_timezone = "datetime.datetime(2022, 12, 3, 8, 3, 52, tzinfo=tzlocal())"
# date_time = date_time_timezone.replace(', tzinfo=tzlocal()', '')
# string = (2022, 12, 3, 8, 3, 52)
# # date_time.strftime("%Y/%m/%d, %H:%M:%S")
# # datetime(date_time)
#
# my_time = datetime.datetime.strftime(string, "%Y/%m/%d, %H:%M:%S")
# print(my_time)



# SDK - CLI like S3 CLI
# Software Development Kit
# Local > AWS S3
# GitHub > AWS S3
