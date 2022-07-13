#!/usr/bin/env python
from datetime import datetime
import boto3
import json


class MessageFactory():

    def create_message(self, **kwargs):
        return Message(**kwargs)


class MessagingBase():

    def __init__(self, queue_name=None):
        self.queue_name = queue_name
        self.client = boto3.client('sqs', region_name='us-west-2')

    def get_queue_url(self):
        response = self.client.get_queue_url(
            QueueName=self.queue_name,
        )
        return response["QueueUrl"]


class MessagingHandler(MessagingBase):
    message_factory_class = MessageFactory

    def __init__(self, message_factory=None, **kwargs):
        super().__init__(**kwargs)
        if message_factory:
            self.message_factory = message_factory
        else:
            self.message_factory = self.message_factory_class()

    def create_queue(self):
        response = self.client.create_queue(
            QueueName=self.queue_name,
            Attributes={
                "DelaySeconds": "0",
                "VisibilityTimeout": "60",
            }
        )
        return response

    def send_message(self, message_type, message):
        message['message_type'] = message_type
        if not 'timestamp' in message:
            message['timestamp'] = datetime.now().isoformat()
        response = self.client.send_message(
            QueueUrl=self.get_queue_url(),
            MessageBody=json.dumps(message)
        )
        return response

    def receive_message(self):
        response = self.client.receive_message(
            QueueUrl=self.get_queue_url(),
            MaxNumberOfMessages=1,
        )        

        count = len(response.get('Messages', []))
        if count > 0:
            message = response['Messages'][0]
            message_body = message["Body"]
            data = json.loads(message_body)
            data['MessageId'] = message['MessageId']
            data['ReceiptHandle'] = message['ReceiptHandle']
            data['queue_name'] = self.queue_name
            deploy_message = self.message_factory.create_message(**data)
            return deploy_message

        return None

    def receive_messages(self, message_type=None):
        messages = []
        found = True
        while(found):
            message = self.receive_message()
            if message is not None:
                if message_type is None or message.message_type == message_type:
                    messages.append(message)
            else:
                found = False

        messages.sort(key=lambda x: (x.timestamp))
        return messages


class Message(MessagingBase):
    message_type = "MessageBase"

    def __init__(self, queue_name=None, timestamp=None, ReceiptHandle=None, MessageId=None, **kwargs):
        super().__init__(queue_name=queue_name)
        self.timestamp = timestamp
        self.receipt_handle = ReceiptHandle
        self.message_id = MessageId
        for key,value in kwargs.items():
            setattr(self, key, value)

    def delete(self):
        self.client.delete_message(
            QueueUrl=self.get_queue_url(),
            ReceiptHandle=self.receipt_handle,
        )

    def get_message_body(self):
        body = {
            'message_type': self.message_type,
        }
        if self.timestamp:
            body['timestamp'] = self.timestamp
        return body
