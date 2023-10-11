import boto3
dynamodb = boto3.resource("dynamodb",region_name = 'ap-northeast-2',
               aws_access_key_id='AKIAV54EX66OQK3L6PVV',
               aws_secret_access_key='')
table = dynamodb.Table('Movies')


results = table.scan()

print(results['Count'], results['ScannedCount'])
items = results['Items']
for i in range(len(items)):
    print(items[i])
    