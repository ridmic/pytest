from process.amqp_connection import Connection
from process.amqp_sender import Publisher
from process.amqp_receiver import Worker
from process.job_config import JobConfig
import json


class DeltaQueueReceiver(Worker):
    def __init__(self, conn):
        self.queue_name = 'delta'

        Worker.__init__(self, conn, self.queue_name)

    def callback(self, ch, method, properties, body):
        print(" [x] Delta Queue Received %r" % body)
        payload = json.loads(str(body.decode('utf8')))

        print(" [x] Processing Job {}".format(payload['job_id']))

        pub = ProductQueueSender(self.connection)
        for item in payload['delta']:
            print(" [x] Product ID: {}".format(item))
            job_detail = {"job_id": item,
                          "timestamp": "2017-01-01T00:00:00",
                          "product_id": item
                          }
            pub.publish(json.dumps(job_detail), 'persist')

        # ACK the job
        ch.basic_ack(delivery_tag=method.delivery_tag)


class ProductQueueSender(Publisher):
    def __init__(self, conn):
        self.queue_name = 'product'

        Publisher.__init__(self, conn, self.queue_name)


# Load our application config
config = JobConfig()

print("Connecting to server...")
connection = Connection(config.aqmp_host())
print("Generating Listener...")
job = DeltaQueueReceiver(connection)
job.consume()
