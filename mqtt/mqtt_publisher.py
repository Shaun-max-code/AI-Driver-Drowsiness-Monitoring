import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("localhost", 1883, 60)

client.publish(
    "smarthome/light",
    "ON"
)

print("Message Sent")

client.disconnect()