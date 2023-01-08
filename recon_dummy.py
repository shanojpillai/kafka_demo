import json
import time

from kafka import KafkaProducer

RECON_KAFKA_TOPIC = "recon_details"
RECON_COUNT = 100

producer = KafkaProducer(bootstrap_servers="localhost:9092")

print("Generating reconciliation after 10 seconds")
print("Create one unique reconciliation every 10 seconds")
time.sleep(10)

for i in range(1, RECON_COUNT):
    data = {
        "item_id": i,
        "bank_id": f"recon_{i}",
        "total_amount": i * 10,
        "source_systems": "NAM",
    }

    producer.send(RECON_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
    send_message = json.dumps(data).encode("utf-8")
    print(f"Done Sending Topic..{send_message}")
    
