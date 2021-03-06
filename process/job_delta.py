from process.amqp_connection import Connection
from process.amqp_sender import Publisher
from process.job_config import JobConfig
import json


class DeltaQueueSender(Publisher):
    def __init__(self, conn):
        self.queue_name = 'delta'

        Publisher.__init__(self, conn, self.queue_name)


def get_delta_job(from_date, to_date):
    """ This is where we would call the webservice to pull through our deltas """
    body = {"job_id": 1,
            "timestamp": "2017-01-01T00:00:00",
            "from": from_date,
            "to": to_date,
            "lastUpdate": from_date,
            "delta": [1, 2, 3, 4, 5, 6, 7, 8, 9]
            }
    return json.dumps(body)


# Load our application config
config = JobConfig()

print("Connecting to server...")
connection = Connection(config.aqmp_host())
print("Generating Payload...")
job = DeltaQueueSender(connection)
payload = get_delta_job('2017-12-01', '2017-12-31')
print("Publishing Payload...")
job.publish(payload, 'persist')
