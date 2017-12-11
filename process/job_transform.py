from process.amqp_connection import Connection
from process.amqp_sender import Publisher
from process.amqp_receiver import Worker
from process.job_config import JobConfig
import json

server_url = 'amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'


class TransformQueueReceiver(Worker):
    def __init__(self, conn):
        self.queue_name = 'transform'

        Worker.__init__(self, conn, self.queue_name)

    def callback(self, ch, method, properties, body):
        print(" [x] Transform Queue Received %r" % body)
        payload = json.loads(str(body.decode('utf8')))

        print(" [x] Processing Job {}".format(payload['job_id']))

        item = payload['product_id']
        job_id = payload['job_id']

        ###############################################
        # This is where all the hard work would be done
        ###############################################

        cpub = CStoreQueueSender(self.connection)
        print(" [x] Product ID: {}".format(item))
        job_detail = {"job_id": job_id,
                      "timestamp": "2017-01-01T00:00:00",
                      "product_id": item,
                      "product_data": "I would be JSON for Product {} to update CS".format(item)
                      }
        cpub.publish(json.dumps(job_detail), 'persist')

        wpub = WStoreQueueSender(self.connection)
        job_detail = {"job_id": job_id,
                      "timestamp": "2017-01-01T00:00:00",
                      "product_id": item,
                      "product_data": "I would be JSON for Product {} to update WS".format(item)
                      }
        wpub.publish(json.dumps(job_detail), 'persist')

        # ACK the job
        ch.basic_ack(delivery_tag=method.delivery_tag)


class CStoreQueueSender(Publisher):
    def __init__(self, conn):
        self.queue_name = 'cstore'

        Publisher.__init__(self, conn, self.queue_name)


class WStoreQueueSender(Publisher):
    def __init__(self, conn):
        self.queue_name = 'wstore'

        Publisher.__init__(self, conn, self.queue_name)


# Load our application config
config = JobConfig()

print("Connecting to server...")
connection = Connection(config.aqmp_host())
print("Generating Listener...")
job = TransformQueueReceiver(connection)
job.consume()
