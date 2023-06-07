"""
Author: Thiago Vilarinho Lemes
Date: 2023-06-06
Description: Projeto com a finalidade de monitorar o Ar e Umidade do Solo com consulta a API e dispositivos IoT. 

Projeto - Monitoramento do Ar e Unidade do Solo com IoT
"""

'''
Function get Weather API
'''
def get_data_api():

    import requests
    import json
    import pandas as pd
    import datetime 
    import os

    '''
    Variables 
    '''
    search_weather      = 'weather'
    latitude            = '-10.186'
    longitude           = '-47.333'
    appid_key           = '751d15d739b39f5b27cbfa029a4ba68a'
    request             = requests.get(f'http://api.openweathermap.org/data/2.5/{search_weather}?lat={latitude}&lon={longitude}&appid={appid_key}&units=metric')

    data_raw                = json.loads(request.content)

    ''' Get Data '''
    current_weather         = data_raw['weather'][0]
    current_main            = data_raw['main']
    current_wind            = data_raw['wind']
    current_sys             = data_raw['sys']
    current_name            = data_raw['name']
    current_date            = data_raw['dt']
    current_date            = datetime.datetime.fromtimestamp(current_date)
    current_date            = current_date.strftime('%Y-%m-%d %H:%M:%S')

    ''' Create dictionary for Dataframe '''
    data_frame = {'date': current_date}
    data_frame.update(current_weather)
    data_frame.update(current_main)
    data_frame.update(current_wind)
    data_frame.update(current_sys)
    data_frame.update({'name': current_name})

    ''' Convert Date '''
    raw_dt                  = pd.DataFrame([data_frame])
    raw_dt['sunrise']       = list(map(lambda x: datetime.datetime.fromtimestamp(x), raw_dt['sunrise']))
    raw_dt['sunset']        = list(map(lambda x: datetime.datetime.fromtimestamp(x), raw_dt['sunset']))
    raw_dt.drop(columns=['id', 'icon'], inplace=True)

    '''
    ##  Reading CSV file ##
    # Variable - located in /config/var_dags.env 
    path_old  - path file
    '''
    path_old        = os.environ['AIRFLOW__PATH__STORAGE']
    raw_dt_old      = pd.read_csv(path_old + 'raw/raw_weather.csv')
    raw_dt_new      = pd.concat([raw_dt, raw_dt_old ])

    '''
    ##  Creating CSV file ##
    # Variable - located in /config/var_dags.env 
    destination_file - path file
    '''
    destination_file = os.environ['AIRFLOW__PATH__STORAGE']
    raw_dt_new.to_csv(destination_file + 'raw/raw_weather.csv', encoding='utf-8', index=False)



