#!/usr/bin/env python
from process.amqp_queue import Queue


class Sender(Queue):
    def __init__(self, queue_conn, queue_name):

        Queue.__init__(self, queue_conn, queue_name, '', queue_name)

    def publish(self, message, mode='none'):

        if (mode == 'persist'):
            self.channel.basic_publish(exchange=self.exchange_name,
                                       routing_key=self.routing_key,
                                       body=message)
            print(" [x] Sent Persistent Message")
        else:
            self.channel.basic_publish(exchange=self.exchange_name,
                                       routing_key=self.routing_key,
                                       body=message)
            print(" [x] Sent Message")


class Publisher(Queue):
    def __init__(self, queue_conn, queue_name):

        Queue.__init__(self, queue_conn, queue_name, queue_name, queue_name)

    def publish(self, message, mode='none'):

        if (mode == 'persist'):
            self.channel.basic_publish(exchange=self.exchange_name,
                                       routing_key=self.routing_key,
                                       body=message,
                                       properties=pika.BasicProperties(
                                           delivery_mode=2,  # make message persistent
                                       ))
            print(" [x] Sent Persistent Message")
        else:
            self.channel.basic_publish(exchange=self.exchange_name,
                                       routing_key=self.routing_key,
                                       body=message)
            print(" [x] Sent Message")
