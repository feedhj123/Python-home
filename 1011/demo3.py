#index Scanning
import boto3,dynamodbinfo

table = dynamodbinfo.table

#1.using get_item
result = table.get_item(
    Key = {
        'Code' : '20050112',
        'Name' : 'Batman Begins',
    }
)

# print(type(result)) # dict
# print(result.keys())
if __name__ == '__main__' : 
    print(result['Item'])
