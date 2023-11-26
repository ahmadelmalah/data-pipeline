import boto3
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='testQ')
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = '({0})'.format(author_name)
    # Print out the body and author (if set)
    print('{0} wrote: {1}'.format(author_text, message.body))
    # Let the queue know that the message is processed
    message.delete()
else:
    print('All messages are processed!')