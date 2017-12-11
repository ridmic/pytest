from process.amqp_connection import Connection
from process.amqp_receiver import Worker
from process.job_config import JobConfig
import json

server_url = 'amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'


class CStoreQueueReceiver(Worker):
    def __init__(self, conn):
        self.queue_name = 'cstore'

        Worker.__init__(self, conn, self.queue_name)

    def callback(self, ch, method, properties, body):
        print(" [x] CStore Queue Received %r" % body)
        payload = json.loads(str(body.decode('utf8')))

        print(" [x] Processing CS Job {}".format(payload['job_id']))

        print(" [x] Product ID: {}".format(payload['product_id']))
        print(" [x] Product CS Data: {}".format(payload['product_data']))

        ###############################################
        # This is where all the hard work would be done
        ###############################################

        # ACK the job
        ch.basic_ack(delivery_tag=method.delivery_tag)


# Load our application config
config = JobConfig()

print("Connecting to server...")
connection = Connection(config.aqmp_host())
print("Generating Listener...")
job = CStoreQueueReceiver(connection)
job.consume()
