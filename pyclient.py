import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("received this", str(message.payload.decode("utf-8")))

mqttBroker = "broker.emqx.io"
client = mqtt.Client("Mantap")
client.connect(mqttBroker)

client.subscribe("TEMPERATURE")
client.on_message = on_message

client.loop_forever()