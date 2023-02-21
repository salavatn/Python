import boto3


def lambda_handler(event, context):
    mys3 = boto3.client('s3')
    content = mys3.list_buckets()
    result = (f"{content}")
    return result

    output = str()

    # try:

    for bucket in result['Buckets']:
        output += bucket['Name'] + "<br>"
    return "<h1><font color=green>S3 Bucket List:</font><h1><br><br>" + output
    # except:
    #     print("<h1><font color=red>[ ERROR ]</font><h1><br><br>")
