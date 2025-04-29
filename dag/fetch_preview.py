from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
from kafka import KafkaProducer
import json

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def fetch_and_push_to_kafka():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    data = response.json()

    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',  # change if needed
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for coin in data:
        producer.send('crypto-topic', value=coin)

    producer.flush()

with DAG(
    dag_id='coingecko_to_kafka',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@hourly',  # run every hour
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='fetch_and_push_to_kafka',
        python_callable=fetch_and_push_to_kafka
    )
