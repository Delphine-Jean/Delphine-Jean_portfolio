from datetime import timedelta, datetime
import json
import pandas as pd
from binance_client import BinanceAPI
import config
import os
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow import DAG
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.gcs_operator import GoogleCloudStorageCreateBucketOperator
import airflow



"""
Python function to export klines historical data from the file binance
"""


def get_klines():
    binances = BinanceAPI(config.API_KEY, config.API_SECRET)

    response = binances.get_klines("BTCUSDT", "1m", startTime="06/01/2021 00:00:00", endTime="06/12/2021 00:00:00")
    data = pd.DataFrame(response)

    data.columns = ['open_time',
                    'open', 'high', 'low', 'clsoe', 'volume',
                    'close_time', 'quote asset volume', 'num_trades',
                    'taker_base_vol', 'taker_quote_vol', 'ignore']

    current_date = datetime.now()
    current_date = current_date.strftime("%d-%m-%Y %H:%M:%S")
    path = os.getcwd()

    #data.to_json('./dags/export.json', orient='index')
    data.to_json("./files/export{}.json", orient='index').format(current_date)
    #print(data)


get_klines()
print(os.getcwd())


defaults_args = {
    'owner': 'Delphine Jean',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='etl_bq',
    default_args=defaults_args,
    description='etl klines historicals to bigquery',
    schedule_interval=timedelta(days=1)
) as dag:


     downloading_files = PythonOperator(
        task_id='downloading_klines',
        python_callable=get_klines
    )

     creating_bucket_gcs =  GoogleCloudStorageCreateBucketOperator(

     )



