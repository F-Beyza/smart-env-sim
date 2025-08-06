# src/mqtt/subscriber.py

import paho.mqtt.client as mqtt
import json

broker = "localhost"
port = 1883
topic = "sensor/data"

def on_connect(client, userdata, flags, rc):
    print("[✓] Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print("[←] Received:", data)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
