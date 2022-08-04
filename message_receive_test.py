#!/usr/bin/env python

from simplesqs.message import MessagingHandler

queue_name = "test_queue_simplesqs"

handler = MessagingHandler(queue_name=queue_name)

while(True):
    messages = handler.batch_receive_messages()
    if len(messages) == 0:
        break
    for message in messages:
        print(message.message)
        message.delete()
