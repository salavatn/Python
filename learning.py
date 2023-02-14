import boto3


def lambda_handler(event, context):
    mys3 = boto3.client('s3')
    result = mys3.list_buckets()
    print(result)

    output = str()
    print(type(output))

    # try:

    for bucket in result['Buckets']:
        output += bucket['Name'] + "<br>"
    return "<h1><font color=green>S3 Bucket List:</font><h1><br><br>" + output
    # except:
    #     print("<h1><font color=red>[ ERROR ]</font><h1><br><br>")

# mydict = {'ResponseMetadata':{'RequestId':'4QZ4YCZRG1Y21BHT','HostId':'kB0aCUSY9Lpe69PoxbWzuEQleZUAlb6Pih8X1alquXpp9AlGY6pj66a4wOdV9GG/wNO0KEaBb4A=','HTTPStatusCode':200,'HTTPHeaders':{'x-amz-id-2':'kB0aCUSY9Lpe69PoxbWzuEQleZUAlb6Pih8X1alquXpp9AlGY6pj66a4wOdV9GG/wNO0KEaBb4A=','x-amz-request-id':'4QZ4YCZRG1Y21BHT','date':'Tue, 14 Feb 2023 08:51:23 GMT','content-type':'application/xml','transfer-encoding':'chunked','server':'AmazonS3'},'RetryAttempts':0},'Buckets':[{'Name':'ns-lab-web','CreationDate': datetime.datetime(2022,12,3,8,3,52,tzinfo=tzlocal())},{'Name':'ns-lab.open-storage','CreationDate':datetime.datetime(2023,2,14,8,45,55,tzinfo=tzlocal())}],'Owner':{'DisplayName':'salavat','ID':'a832a8b8a4e6cf3a0ca798daa02b087110234b6db836b61904789188f9615fb0'}}
# mylist = [
#   "Result type:\t<class 'dict'> \nResult is:\t {'ResponseMetadata': {'RequestId': 'QQJCNE8PAX3CDNV3', 'HostId': 'RrI/i05GYb2moGyGPaCpg9Unxr8Vp1Jd5hiDu9BrDNr1IC1oQWONFgJYk+eOusZcIkNDFKp8kYU=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'RrI/i05GYb2moGyGPaCpg9Unxr8Vp1Jd5hiDu9BrDNr1IC1oQWONFgJYk+eOusZcIkNDFKp8kYU=', 'x-amz-request-id': 'QQJCNE8PAX3CDNV3', 'date': 'Tue, 14 Feb 2023 09:06:50 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'ns-lab-web', 'CreationDate': datetime.datetime(2022, 12, 3, 8, 3, 52, tzinfo=tzlocal())}, {'Name': 'ns-lab.open-storage', 'CreationDate': datetime.datetime(2023, 2, 14, 8, 45, 55, tzinfo=tzlocal())}], 'Owner': {'DisplayName': 'salavat', 'ID': 'a832a8b8a4e6cf3a0ca798daa02b087110234b6db836b61904789188f9615fb0'}}"
# ]
# print(mylist)
