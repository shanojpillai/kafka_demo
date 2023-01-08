import json

from kafka import KafkaConsumer
from kafka import KafkaProducer


RECON_KAFKA_TOPIC = "recon_details"
RECON_DONE_KAFKA_TOPIC = "recon_done"

consumer = KafkaConsumer(
    RECON_KAFKA_TOPIC, 
    bootstrap_servers="localhost:9092"
)
producer = KafkaProducer(bootstrap_servers="localhost:9092")


print("Listening...")
while True:
    for message in consumer:
        print("Reading current transaction..")
        #decoding and turning it to dictionary
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        item_id = consumed_message["item_id"]
        total_amount = consumed_message["total_amount"]
        data = {
            "recon_id": item_id,
            "total_amount": total_amount,
            "recon_status": "Done"
        }
        print("Reconciliation Done!..")
        producer.send(RECON_DONE_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
        write_message = json.dumps(data).encode("utf-8")
        print(write_message)
