#!/usr/bin/env python
from process.amqp_connection import Connection


class Queue:
    def __init__(self, queue_conn, queue_name, exchange_name, routing_key, queue_durable=True):

        # Save our connection object
        self.connection = None
        if isinstance(queue_conn, Connection):
            self.connection = queue_conn

        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.queue_durable = queue_durable
        self.channel = self.connection.conn().channel()

        # Set up our channel
        self.channel_config()

        print(" [x] Attached to Exchange: {}, Queue: {}, Route: {}".format(self.exchange_name,
                                                                           self.queue_name,
                                                                           self.routing_key))

    def channel_config(self):

        # Set up our channel
        if self.exchange_name != '':
            self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct', durable=True)
        self.channel.queue_declare(queue=self.queue_name, durable=self.queue_durable)
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name)


class SubscriberQueue(Queue):
    def channel_config(self):
        # Set up our channel
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='fanout')
        result = self.channel.queue_declare(exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name)
