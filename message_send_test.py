#!/usr/bin/env python

from simplesqs.message import MessagingHandler

queue_name = "test_queue_simplesqs"

handler = MessagingHandler(queue_name=queue_name)

handler.create_queue()

for x in range(10):
    handler.send_message(message_type='test', message={'message': f"Hello world {x}!"})



