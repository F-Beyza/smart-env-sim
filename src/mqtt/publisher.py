# src/mqtt/publisher.py

import paho.mqtt.client as mqtt
import json
import time
import random

broker = "localhost"
port = 1883
topic = "sensor/data"

client = mqtt.Client()

def generate_fake_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    client.connect(broker, port, 60)
    print("[✓] Connected to MQTT Broker")

    while True:
        payload = generate_fake_data()
        client.publish(topic, json.dumps(payload))
        print("[→] Published:", payload)
        time.sleep(3)

if __name__ == "__main__":
    main()
