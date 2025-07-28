import threading
from kafka import KafkaConsumer
import json
import time
from kafka.errors import NoBrokersAvailable


def consume_logs():
    while True:
        try:
            consumer = KafkaConsumer(
                'logs',
                bootstrap_servers='kafka:9092',
                group_id='log-viewer',
                auto_offset_reset='earliest',
                enable_auto_commit=True,
                value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
            print("Kafka consumer thread started")
            with open('/app/kafka_consumed.log', 'a', encoding='utf-8') as f:
                for msg in consumer:
                    data = msg.value
                    log_line = (
                        f"[{data['user']} @ {data['route']}] → "
                        f"{data['message']}\n"
                    )
                    f.write(log_line)
                    f.flush()
        except NoBrokersAvailable:
            print("Kafka broker not available, retrying in 5 seconds...")
            time.sleep(5)


def start_consumer_thread():
    t = threading.Thread(target=consume_logs, daemon=True)
    t.start()
