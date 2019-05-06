from transactions import create_random_transaction
from kafka import KafkaProducer
from time import sleep
import json
import os

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("KAFKA_TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = int(os.environ.get("TRANSACTIONS_PER_SECOND"))
TIME_SLEEP = 1.0 / TRANSACTIONS_PER_SECOND
REDIS_SERVER_URL = os.environ.get("REDIS_SERVER_URL")

if __name__ == "__main__":

    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                             value_serializer=lambda x: json.dumps(x).encode())

    while True:

        transaction = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        producer.flush()
        sleep(TIME_SLEEP)
