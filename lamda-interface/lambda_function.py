import json
import boto3

def lambda_handler(event, context):
    
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='testQ')
    
    
    # Create a new message
    response = queue.send_message(MessageBody='Sample Message3!', MessageAttributes={
        'Author': {
            'StringValue': 'Ahmad',
            'DataType': 'String'
        }
    })
    return {
        'statusCode': 200,
        'body': json.dumps(response.get('MessageId'))
    }
