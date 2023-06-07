"""
Author: Thiago Vilarinho Lemes
Date: 2023-06-03
Description: Projeto com a finalidade de monitorar o Ar e Umidade do Solo com consulta a API e dispositivos IoT. 

Projeto - Monitoramento do Ar e Unidade do Solo com IoT
"""

'''
Function get Weather Local
'''
def get_weather_local():
    '''
    Import libs
    '''
    from kafka import KafkaConsumer
    import os
    import time
    import pandas as pd
    '''
    Variables
    '''
    topic_data      = os.environ['AIRFLOW__TOPIC__KAFKA'] 

    '''
    Get Consumer Kafka
    '''
    consumer = KafkaConsumer(
        topic_data,
        bootstrap_servers   = 'broker:29092'
        # group_id='group-topic-data'
    )

    for mensage in consumer:
        temp    = {'temp_local': str(mensage.value[0:4]).replace("b", '').replace("'", '').replace(" ", '')}
        humid   = {'humid_local': str(mensage.value[6:10]).replace("b", '').replace("'", '').replace(" ", '')}

        '''
        ##  Creating CSV file ##
        # Variable - located in /config/var_dags.env 
        destination_file - path file
        '''
        destination_file = os.environ['AIRFLOW__PATH__STORAGE']
        th_df = temp
        th_df.update(humid)
        th_df = pd.DataFrame([th_df])
        th_df.to_csv(destination_file + 'raw/th_df.csv', encoding='utf-8', index=False) 
        time.sleep(3) 
        exit()
