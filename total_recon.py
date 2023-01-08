import json

from kafka import KafkaConsumer


RECON_DONE_KAFKA_TOPIC = "recon_done"


consumer = KafkaConsumer(
    RECON_DONE_KAFKA_TOPIC, 
    bootstrap_servers="localhost:9092"
)

total_recon_count = 0

print("Listening...")
while True:
    for message in consumer:
        print("Updating Recon Count..")
        consumed_message = json.loads(message.value.decode())
        total_recon_count += 1
        print(f"Total recon: {total_recon_count}")
        
