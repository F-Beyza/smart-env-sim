# src/mqtt/publisher.py

import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/data"

client = mqtt.Client()

def connect_mqtt():
    client.connect(BROKER, PORT, 60)
    print(f"[✓] Connected to MQTT Broker at {BROKER}:{PORT}")

def publish_loop():
    while True:
        data = {
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "humidity": round(random.uniform(30.0, 60.0), 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        payload = json.dumps(data)
        client.publish(TOPIC, payload)
        print(f"[→] Published to {TOPIC}: {payload}")
        time.sleep(3)

if __name__ == "__main__":
    connect_mqtt()
    publish_loop()
