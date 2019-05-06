from kafka import KafkaConsumer, KafkaProducer
import json
import os

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("KAFKA_TRANSACTIONS_TOPIC")
LEGIT_TOPIC = os.environ.get("KAFKA_LEGIT_TOPIC")
FRAUD_TOPIC = os.environ.get("KAFKA_FRAUD_TOPIC")

def is_suspicius(transaction):
    return transaction["amount"] >= 900

if __name__ == "__main__":

    consumer = KafkaConsumer(TRANSACTIONS_TOPIC,
                             bootstrap_servers=KAFKA_BROKER_URL,
                             value_deserializer=lambda x: json.loads(x.decode()))

    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                             value_serializer=lambda x: json.dumps(x).encode())

    for message in consumer:
        transaction = message.value
        topic = FRAUD_TOPIC if is_suspicius(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)
