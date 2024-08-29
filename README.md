# Simple SQS

Provides a simple class-based wrapper around AWS SQS.

## Quick start

Install with pip:

    pip install simplesqs

Creating a queue:

    from simplesqs.message import MessagingHandler

    queue_name = "test_queue_simplesqs"
    handler = MessagingHandler(queue_name=queue_name)
    handler.create_queue()

Sending a message:

    from simplesqs.message import MessagingHandler

    queue_name = "test_queue_simplesqs"
    handler = MessagingHandler(queue_name=queue_name)
    handler.send_message(message_type='test', message={'message': f"Hello world!"})

Reading messages:

    from simplesqs.message import MessagingHandler

    queue_name = "test_queue_simplesqs"
    handler = MessagingHandler(queue_name=queue_name)

    while True:
        messages = handler.batch_receive_messages(message_type='test')
        if len(messages) == 0:
            break
        for message in messages:
            print(message.message)
            message.delete()
