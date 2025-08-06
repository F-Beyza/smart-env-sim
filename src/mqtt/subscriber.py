# src/mqtt/subscriber.py

import paho.mqtt.client as mqtt
import json
from mongo_handler.mongo_handler import MongoHandler

mongo_handler = MongoHandler()

def on_connect(client, userdata, flags, rc):
    print("[✓] Connected to MQTT broker")
    client.subscribe("sensor/data")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("[•] Message received:", payload)

    try:
        data = json.loads(payload)
        mongo_handler.insert_data(data)
        print("[✓] Data inserted into MongoDB")
    except json.JSONDecodeError:
        print("[✗] Invalid JSON format")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
print("[•] Waiting for messages...")
client.loop_forever()
