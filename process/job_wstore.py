from amqp_connection import Connection
from amqp_reciever import Worker
import json


server_url='amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'

class WStoreQueueReceiver(Worker):

  def  __init__(self, conn):
    self.queue_name = 'wstore'

    Worker.__init__(self, conn, self.queue_name)

  def callback(self, ch, method, properties, body):
    print(" [x] WStore Queue Received %r" % body)
    payload = json.loads(str(body.decode('utf8')))

    print(" [x] Procesing WS Job {}".format(payload['job_id']))

    print(" [x] Product ID: {}".format(payload['product_id']))
    print(" [x] Product WS Data: {}".format(payload['product_data']))

    ###############################################
    # This is where all the hard work would be done
    ###############################################

    # ACK the job
    ch.basic_ack(delivery_tag = method.delivery_tag)


conn = Connection(server_url)
job = WStoreQueueReceiver(conn)
try:
  job.consume()
except KeyboardInterrupt:
  job.channel.stop_consuming()
  print('Worker loop terminated by Ctrl-C')
