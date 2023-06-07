"""
Author: Thiago Vilarinho Lemes
Date: 2023-05-28
Description: Projeto com a finalidade de monitorar o Ar e Umidade do Solo com consulta a API e dispositivos IoT. 

Projeto - Monitoramento do Ar e Unidade do Solo com IoT
"""

'''
## Importing Libraries ##
'''
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from get_data_api import get_data_api
from kafka_consumer import get_weather_local


'''
# Variables - located in /config/var_dags.env
'''


'''
## DAG parameters ##
'''
with DAG(
    dag_id='dag_projeto_ground_air', 
    tags=['ground', 'air', 'firebase'],
    start_date=datetime(2023, 6, 6), 
    schedule_interval='@daily',
	catchup=False
    ) as dag:

    # Start
    ts = DummyOperator(task_id='START')

    # 1° task - check se existe o arquivo local 
    t1  = PythonOperator(
        task_id='GET_DATA_API', 
        python_callable=get_data_api
    )

    t2  = PythonOperator(
        task_id='KAFKA_DATA_COMSUMER', 
        python_callable=get_weather_local
    )



    # Start
    te = DummyOperator(task_id='END')
   


    ts >> [t1, t2]   >> te