import os
from datetime import timedelta, datetime

import pandas as pd
"""from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.gcs_operator import GoogleCloudStorageCreateBucketOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator"""


import config
from binance_client import BinanceAPI

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
    current_date = current_date.strftime("%d-%m-%Y-%Hh%Mmin%Ss")
    path = os.getcwd()
    data.to_json(r'{}/files/export{}.json'.format(path, current_date), orient='index')
    print(data)


get_klines()
print(os.getcwd())


"""defaults_args = {
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

     CreateBucket = GoogleCloudStorageCreateBucketOperator(
         task_id="CreateNewBucket",
         bucket_name="test-bucket",
         storage_class="MULTI_REGIONAL",
         location="EU",
         labels={"env": "dev", "team": "airflow"},
     )

     CreateTable = BigQueryCreateEmptyTableOperator(
         task_id='BigQueryCreateEmptyTableOperator_task',
         dataset_id='ODS',
         table_id='Employees',
         project_id='internal-gcp-project',
         schema_fields=[{"name": "emp_name", "type": "STRING", "mode": "REQUIRED"},
                        {"name": "salary", "type": "INTEGER", "mode": "NULLABLE"}],
         bigquery_conn_id='airflow-conn-id-account',
         google_cloud_storage_conn_id='airflow-conn-id'
     )

     load_historical_klines_to_bq = GoogleCloudStorageToBigQueryOperator(
         task_id='load_historical_klines',
         bucket=gs_bucket,
         source_objects=['cities/us-cities-demographics.csv'],
         destination_project_dataset_table=f'{project_id}:{staging_dataset}.us_cities_demo',
         schema_object='cities/us_cities_demo.json',
         write_disposition='WRITE_TRUNCATE',
         source_format='csv',
         field_delimiter=';',
         skip_leading_rows=1
     )"""





