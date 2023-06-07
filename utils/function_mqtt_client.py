import paho.mqtt.client as mqtt
import time
import os

'''
MQTT broker information variables
'''
# broker_address  = os.environ['AIRFLOW__IP__BROKER'] 
# broker_port     = os.environ['AIRFLOW__PORT__BROKER'] 
# topic_temp      = os.environ['AIRFLOW__TOPIC__TEMP'] 
# topic_humid     = os.environ['AIRFLOW__TOPIC__HUMID'] 
# sleep_broker    = os.environ['AIRFLOW__SLEEP__BROKER'] 

broker_address  = '192.168.0.21'
broker_port     = 1883
topic_temp      = 'temp/'
topic_humid     = 'humid/'
sleep_broker    = 2


'''
Configure MQTT client settings
'''
client = mqtt.Client()


'''
Callback function for when the connection to the broker is established
'''
def on_connect(client, userdata, flags, rc):
    print("Connected to the MQTT broker")
    client.subscribe(topic_temp)  
    client.subscribe(topic_humid) 


'''
Callback function for when a new message arrives
'''
def on_message(client, userdata, msg):
    print("Mensagem recebida: " + str(msg.payload.decode()))


'''
Bind callback functions to the MQTT client
'''
client.on_connect = on_connect
client.on_message = on_message


'''
Connect to the MQTT broker
'''
client.connect(broker_address, broker_port, 60)


'''
Start the message receiving loop
'''
while True:
    client.loop_start()
    time.sleep(sleep_broker)
