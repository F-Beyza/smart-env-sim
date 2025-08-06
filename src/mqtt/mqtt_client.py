import paho.mqtt.client as mqtt
import json
from mongo_handler.mongo_handler import MongoHandler

class MQTTClient:
    def __init__(self, topic, broker_host="localhost", broker_port=1883):
        self.topic = topic
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.mongo_handler = MongoHandler()  # varsayılan db: env_data, collection: sensor_data

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print("[✓] Connected with result code " + str(rc))
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            print("[•] MQTT message received:", payload)
            self.mongo_handler.insert_data(payload)
        except Exception as e:
            print("[!] Error handling message:", e)

    def start(self):
        self.client.connect(self.broker_host, self.broker_port, 60)
        print("[•] Starting MQTT loop...")
        self.client.loop_forever()
