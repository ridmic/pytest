#!/usr/bin/env python
import pika


class Queue:

    def __init__(self, queue_name, exchange_name, routing_key, server_url):

        self.connection = None

        self.connection = pika.BlockingConnection(pika.URLParameters(server_url))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=queue_name)

        self.exchange = exchange_name
        self.routing_key = routing_key
        pass


    def close(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = None


    def __del__(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = None



class Publisher(Queue):

    def __init__(self, queue_name, server_url):

        Queue.__init__(self, queue_name, '', queue_name, server_url)


    def publish(self, message):

        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=message)
        print(" [x] Sent Message")


class Reciever(Queue):

    def __init__(self, queue_name, server_url):

        Queue.__init__(self, queue_name, '', queue_name, server_url)

        self.channel.basic_consume(self.callback, queue=queue_name, no_ack=True)

    def Consume(self):

        self.channel.start_consuming()


    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)



class Worker:
    pass


class Subscriber:
    pass



server_url='amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'

print('creating')
#pub = Publisher('hello', server_url)
sub = Reciever('hello', server_url)

# pub.publish('hello mike')


sub.close()
print('done')
