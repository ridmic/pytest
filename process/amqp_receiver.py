#!/usr/bin/env python
from process.amqp_queue import Queue, SubscriberQueue


class Receiver(Queue):
    def __init__(self, queue_conn, queue_name):
        Queue.__init__(self, queue_conn, queue_name, '', queue_name)

        self.channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)

    def consume(self):
        try:
            print(" [x] Entering consume loop...")
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
            print(' [x] Worker loop terminated by Ctrl-C')

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)


class Worker(Queue):
    def __init__(self, queue_conn, queue_name):
        Queue.__init__(self, queue_conn, queue_name, queue_name, queue_name)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.callback, queue=self.queue_name)

    def consume(self):
        try:
            print(" [x] Entering consume loop...")
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
            print(' [x] Worker loop terminated by Ctrl-C')

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)

        ch.basic_ack(delivery_tag=method.delivery_tag)


class Subscriber(SubscriberQueue):
    def __init__(self, queue_conn, queue_name):
        SubscriberQueue.__init__(self, queue_conn, queue_name, queue_name, queue_name)

        self.channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)

    def consume(self):
        try:
            print(" [x] Entering consume loop...")
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()
            print(' [x] Worker loop terminated by Ctrl-C')

    def callback(self, ch, method, properties, body):
        print(" [x] Subscriber Received %r" % body)
