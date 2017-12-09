from amqp_connection import Connection
from amqp_sender import Publisher
from amqp_reciever import Worker
import json

server_url = 'amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'


class ProductQueueReceiver(Worker):
    def __init__(self, conn):
        self.queue_name = 'product'

        Worker.__init__(self, conn, self.queue_name)

    def callback(self, ch, method, properties, body):
        print(" [x] Product Queue Received %r" % body)
        payload = json.loads(str(body.decode('utf8')))

        print(" [x] Procesing Job {}".format(payload['job_id']))

        pub = TransformQueueSender(self.connection)
        item = payload['product_id']
        job_id = payload['job_id']
        print(" [x] Product ID: {}".format(item))
        job_detail = {"job_id": job_id,
                      "timestamp": "2017-01-01T00:00:00",
                      "product_id": item,
                      "product_data": "I would be JSON for Product {}".format(item)
                      }
        pub.publish(json.dumps(job_detail), 'persist')

        # ACK the job
        ch.basic_ack(delivery_tag=method.delivery_tag)


class TransformQueueSender(Publisher):
    def __init__(self, conn):
        self.queue_name = 'transform'

        Publisher.__init__(self, conn, self.queue_name)


conn = Connection(server_url)
job = ProductQueueReceiver(conn)
try:
    job.consume()
except KeyboardInterrupt:
    job.channel.stop_consuming()
    print('Worker loop terminated by Ctrl-C')
