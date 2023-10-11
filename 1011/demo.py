import boto3
resource = boto3.resource("dynamodb",region_name = 'ap-northeast-2',
               aws_access_key_id='AKIAV54EX66OQK3L6PVV',
               aws_secret_access_key='')

client = boto3.client('dynamodb')

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Code',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },
    ],
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'Code',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE'   
        }
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Movies'
        },
    ],
    TableClass='STANDARD',
    DeletionProtectionEnabled=True,
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)