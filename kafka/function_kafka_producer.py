"""
Author: Thiago Vilarinho Lemes
Date: 2023-05-28
Description: Projeto com a finalidade de monitorar o Ar e Umidade do Solo com consulta a API e dispositivos IoT. 

Projeto - Monitoramento do Ar e Unidade do Solo com IoT
"""

'''
Import libs
'''
from kafka import KafkaProducer
import paho.mqtt.client as mqtt
import os
import time


# broker_address  = os.environ['AIRFLOW__IP__BROKER'] 
# broker_port     = os.environ['AIRFLOW__PORT__BROKER'] 
# topic_temp      = os.environ['AIRFLOW__TOPIC__TEMP'] 
# topic_humid     = os.environ['AIRFLOW__TOPIC__HUMID'] 
# topic_data      = os.environ['AIRFLOW__TOPIC__KAFKA'] 
# sleep_broker    = os.environ['AIRFLOW__SLEEP__BROKER'] 

'''
Variables
'''
broker_address  = '192.168.0.21'
broker_port     = 1883
topic_temp      = 'temp/'
topic_humid     = 'humid/'
topic_data      = 'topic_data'
sleep_broker    = 3


'''
Configure MQTT client settings
'''
client = mqtt.Client()


'''
Callback function for when the connection to the broker is established
'''
def on_connect(client, userdata, flags, rc):
    print("CONNECTED TO THE MQTT BROKER...")
    client.subscribe(topic_temp)  
    # client.subscribe(topic_humid) 


'''
Callback function for when a new message arrives
'''
i = 0
def on_message(client, userdata, msg):
    global i
    topic_msg = str(msg.payload.decode())
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send(topic_data,topic_msg)
    os.system('clear')
    i = i + 1
    print("CONNECTED TO THE MQTT BROKER...")
    print('Running BROKER KAFKA...')
    print('READINGS: ' + str(i))

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