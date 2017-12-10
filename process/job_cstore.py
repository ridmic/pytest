from amqp_connection import Connection
from amqp_reciever import Worker
import json

server_url = 'amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'


class CStoreQueueReceiver(Worker):
    def __init__(self, conn):
        self.queue_name = 'cstore'

        Worker.__init__(self, conn, self.queue_name)

    def callback(self, ch, method, properties, body):
        print(" [x] CStore Queue Received %r" % body)
        payload = json.loads(str(body.decode('utf8')))

        print(" [x] Procesing CS Job {}".format(payload['job_id']))

        print(" [x] Product ID: {}".format(payload['product_id']))
        print(" [x] Product CS Data: {}".format(payload['product_data']))

        ###############################################
        # This is where all the hard work would be done
        ###############################################

        # ACK the job
        ch.basic_ack(delivery_tag=method.delivery_tag)


conn = Connection(server_url)
job = CStoreQueueReceiver(conn)
try:
    job.consume()
except KeyboardInterrupt:
    job.channel.stop_consuming()
    print('Worker loop terminated by Ctrl-C')
