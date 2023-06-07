#  Projeto GroundAir

<p style="color:red">EM DESENVOLVIMENTO</p>

Este projeto tem como objetivo principal a criação de um <b>Big Data</b> para o monitoramento de temperatura máxima e mínima, pressão atmosférica, umidade do solo, entre outros dados, utilizando a API <b>Open Weather</b> e sensores <b>IoT</b> conectados ao computador por meio de <b>Wireless</b> - conexão sem fio. 

Foi utilizado o protocolo <b>MQTT - Mosquitto</b> juntamente com o <b>Kafka</b> para realizar a coleta dos dados dos sensores e da API. Após a coleta dos dados estes são capturados pelo <b>Airflow</b> onde passam por processamento com <b>Spark</b> e são armazenados no <b>Firebase</b>.

Foi criado as camadas <b>BRONZE/RAW</b>, <b>SILVER</b> e <b>GOLD</b> para o <b>Data Lakehouse</b>.

![](/images/print.png)

<hr>


## Programas e Bibliotecas Utilizados:</B>

* VSCode
* Docker Desktop
* Airflow 2.5.1
* Kafka
* Node-Red
* PostgreSQL 13
* PGAdmin4
* Protocolo MQTT - Mosquitto
* apache-airflow-providers-apache-spark==4.0.0
* apache-airflow-providers-google==10.1.0rc1
* pyspark==3.2.1
* delta-spark==2.0.0
* google-cloud-storage
* firebase
* firebase_admin
* kafka-python

<hr>

## Contatos 

Autor: <i>Thiago Vilarinho Lemes</i>

Email: `contatothiagolemes@gmail.com`

Likedin: [`Thiago Vilarinho Lemes`](https://www.linkedin.com/in/thiago-l-b1232727/)

<hr>

## Dicionário de Dados da API

* coord
    * lon Longitude do local
    * lat Latitude do local

* weather (mais informações Códigos de condições meteorológicas)
    * id - ID da condição do tempo
    * main - Grupo de parâmetros climáticos (Chuva, Neve, Extremo, etc.)
    * description - Condição do tempo dentro do grupo. Você pode obter a saída em seu idioma. Saber mais
    * icon - ID do ícone do tempo
* main
    * temp - Temperatura. Padrão da unidade: Kelvin, métrico: Celsius, imperial: Fahrenheit.
    * feels_like - Temperatura. Este parâmetro de temperatura é responsável pela percepção humana do clima. Padrão da unidade: Kelvin, métrico: Celsius, imperial: Fahrenheit.
    * pressure - Pressão atmosférica (no nível do mar, se não houver dados sea_level ou grnd_level), hPa
    main.humidity Umidade, %
    * temp_min - Temperatura mínima no momento. Esta é a temperatura mínima observada atualmente (dentro de grandes megalópoles e áreas urbanas). Padrão da unidade: Kelvin, métrico: Celsius, imperial: Fahrenheit.
    * temp_max - Temperatura máxima no momento. Esta é a temperatura máxima atualmente observada (dentro de grandes megalópoles e áreas urbanas). Padrão da unidade: Kelvin, métrico: Celsius, imperial: Fahrenheit.
    * sea_level - Pressão atmosférica ao nível do mar, hPa
    * grnd_level - Pressão atmosférica no nível do solo, hPa
* visibility - Visibilidade, medidor. O valor máximo da visibilidade é de 10km
* wind
    *  speed - Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
    * deg - Wind direction, degrees (meteorological)
    * gust - Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
* clouds
    * all - Nebulosidade, %
* rain
    * 1h - (quando disponível) Volume de chuva na última 1 hora, mm. Observe que apenas mm como unidades de medida estão disponíveis para este parâmetro.
    * 3h - (quando disponível) Volume de chuva nas últimas 3 horas, mm. PPor favor, note que apenas mm como unidades de medida estão disponíveis para este parâmetro.
* snow
    * 1h - (quando disponível) Volume de neve na última 1 hora, mm. Observe que apenas mm como unidades de medida estão disponíveis para este parâmetro.
    * 3h - (quando disponível)Volume de neve nas últimas 3 horas, mm. Observe que apenas mm como unidades de medida estão disponíveis para este parâmetro.
* dt - Hora do cálculo dos dados, unix, UTC
* sys

    * type - Parâmetro interno

    * id - Parâmetro interno

    * message - Parâmetro interno

    * country - Código do país (GB, JP etc.)

    * sunrise -  Hora do nascer do sol, unix, UTC
    
    * sunset - Horário do pôr do sol, unix, UTC

* timezone - mudança de fuso horário em segundos de UTC

* id - ID da cidade. Observe que a funcionalidade integrada do geocodificador foi descontinuada. Saiba mais aqui.

* name - Nome da cidade. Observe que a funcionalidade integrada do geocodificador foi descontinuada. Saiba mais aqui.

* cod - Parâmetro interno

<hr>

## Link´s de referências

Tutorial Kafka com protocolo MQTT - https://www.youtube.com/watch?v=FDCTQ47oXUg

Tutorial - https://www.youtube.com/watch?v=zaA6PTORb1Y

Tutorial - https://www.youtube.com/watch?v=L38-6ilGeKE

List Tutorial - https://www.youtube.com/results?search_query=mqtt+com+cafka

Conversor <i>on-line</i> de datas - https://www.unixtimestamp.com/

Site OpenWeather - https://openweathermap.org/


