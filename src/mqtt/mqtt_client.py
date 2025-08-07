    #    import paho.mqtt.client as mqtt
     #   import json
      #  from mongo_handler.mongo_handler import MongoHandler
#
 #       class MQTTClient:
  #          def __init__(self, topic, broker_host="localhost", broker_port=1883):
   #             self.topic = topic
    #            self.broker_host = broker_host
     #           self.broker_port = broker_port
      #          self.mongo_handler = MongoHandler()  # varsayılan db: env_data, collection: sensor_data
#
 #               self.client = mqtt.Client()
  #              self.client.on_connect = self.on_connect
   #             self.client.on_message = self.on_message
#
 #           def on_connect(self, client, userdata, flags, rc):
  #              print("[✓] Connected with result code " + str(rc))
   #             client.subscribe(self.topic)
#
 #           def on_message(self, client, userdata, msg):
  #              try:
   #                 payload = json.loads(msg.payload.decode())
    #                print("[•] MQTT message received:", payload)
     #               self.mongo_handler.insert_data(payload)
      #          except Exception as e:
       #             print("[!] Error handling message:", e)
#
 #           def start(self):
  #              self.client.connect(self.broker_host, self.broker_port, 60)
   #             print("[•] Starting MQTT loop...")
    #            self.client.loop_forever()


# src/mqtt/mqtt_client.py

import paho.mqtt.client as mqtt
import json
import logging
from data_handler.data_handler import DataHandler  # MongoDB handler class

from utils.logger import setup_logger
logger = setup_logger("MQTTClient")

class MQTTClient:
    def __init__(self, topic, broker_host="localhost", broker_port=1883):
        self.topic = topic
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client = mqtt.Client()

        # Callback binding
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.on_log = self.on_log

        # MongoDB handler
        self.data_handler = DataHandler()

    def connect(self):
        try:
            self.client.connect(self.broker_host, self.broker_port, 60)
            logger.info(f"Connected to MQTT broker at {self.broker_host}:{self.broker_port}")
        except Exception as e:
            logger.error(f"Connection failed: {e}")

    def loop_forever(self):
        logger.info("Starting MQTT loop...")
        self.client.loop_forever()

    # --- Callback functions ---

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Successfully connected to broker")
            self.client.subscribe(self.topic)
            logger.info(f"Subscribed to topic: {self.topic}")
        else:
            logger.error(f"Connection failed with code {rc}")

    def on_disconnect(self, client, userdata, rc):
        logger.warning(f"Disconnected with code {rc}")

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            logger.info(f"Received message on {msg.topic}: {payload}")
            self.data_handler.insert_data(payload)
        except Exception as e:
            logger.error(f"Failed to process message: {e}")

    def on_publish(self, client, userdata, mid):
        logger.debug(f"Message {mid} published successfully")

    def on_log(self, client, userdata, level, buf):
        logger.debug(f"LOG: {buf}")
