import boto3
dynamodb = boto3.resource("dynamodb",region_name = 'ap-northeast-2',
               aws_access_key_id='AKIAV54EX66OQK3L6PVV',
               aws_secret_access_key='')
table = dynamodb.Table('Movies')
client = boto3.client('dynamodb')
item = {
    'Code' :'19780080',
    'Name' :'StarWars',
    'Genre' : 'SF', 
    'Date' : '1978-04-12', 
    'Director' : '조지 루카스',
    'Actor' : '마흐 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
}
table.put_item(Item = item)
