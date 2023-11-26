import boto3
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='testQ')


# Create a new message
response = queue.send_message(MessageBody='Sample Message!', MessageAttributes={
    'Author': {
        'StringValue': 'Ahmad',
        'DataType': 'String'
    }
})


# The response is NOT a resource, but gives you a message ID and MD5
print(response.get('MessageId'))
