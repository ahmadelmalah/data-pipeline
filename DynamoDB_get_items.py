import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test')
items = table.scan().get('Items')
for item in items:
    print(item['name'])