# src/mqtt/subscriber.py

<<<<<<< HEAD
 #       import paho.mqtt.client as mqtt
  #      import json
   #     from mongo_handler.mongo_handler import MongoHandler
#
 #       mongo_handler = MongoHandler()
#
 #       def on_connect(client, userdata, flags, rc):
  #          print("[✓] Connected to MQTT broker")
 #           client.subscribe("sensor/data")
#
  #      def on_message(client, userdata, msg):
   #         payload = msg.payload.decode()
    #        print("[•] Message received:", payload)
#
     #       try:
 #               data = json.loads(payload)
  #              mongo_handler.insert_data(data)
   #             print("[✓] Data inserted into MongoDB")
    #        except json.JSONDecodeError:
     #           print("[✗] Invalid JSON format")
#
 #       client = mqtt.Client()
  #      client.on_connect = on_connect
   #     client.on_message = on_message
#
 #       client.connect("localhost", 1883, 60)
  #      print("[•] Waiting for messages...")
   #     client.loop_forever()
=======
import paho.mqtt.client as mqtt
import json

import sys
import os

# Bir üst dizini sys.path'a ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from mongo_handler.mongo_handler import MongoHandler
>>>>>>> refactor-mqtt-callbacks



# src/mqtt/subscriber.py



from mqtt.mqtt_client import MQTTClient


def main():
    client = MQTTClient(topic="sensor/data")
    client.connect()
    client.loop_forever()

if __name__ == "__main__":
    main()
