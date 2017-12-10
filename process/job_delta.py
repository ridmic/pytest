from amqp_connection import Connection
from amqp_sender import Publisher
import json

server_url = 'amqp://azyejlhd:jKYvB_Zd6_NHwvp9s7BzU86hThCdTT8R@spider.rmq.cloudamqp.com/azyejlhd'


class DeltaQueueSender(Publisher):
    def __init__(self, conn):
        self.queue_name = 'delta'

        Publisher.__init__(self, conn, self.queue_name)


""" This is where we would call the webservice to pull through our deltas """


def getDeltaJob(fromDate, toDate):
    payload = {"job_id": 1,
               "timestamp": "2017-01-01T00:00:00",
               "lastUpdate": fromDate,
               "delta": [1, 2, 3, 4, 5, 6, 7, 8, 9]
               }
    return json.dumps(payload)


conn = Connection(server_url)
job = DeltaQueueSender(conn)
payload = getDeltaJob('2017-12-01', '2017-12-31')
job.publish(payload, 'persist')
