# src/mqtt/subscriber.py


import paho.mqtt.client as mqtt
import json

import sys
import os

# Bir üst dizini sys.path'a ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from mongo_handler.mongo_handler import MongoHandler
from mqtt.mqtt_client import MQTTClient


def main():
    client = MQTTClient(topic="sensor/data")
    client.connect()
    client.loop_forever()

if __name__ == "__main__":
    main()
