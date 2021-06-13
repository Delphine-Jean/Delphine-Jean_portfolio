from google.cloud import bigquery
from google.oauth2 import service_account

client = bigquery.Client()
filename = ''
dataset_id = 'project_crypto_etl'
table_id = 'historical_klines_2019_2020_BTC'

dataset_ref = client.dataset(dataset_id)
table_ref =client.get_table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.autodetect = True

with open(filename, "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        location = 'europe-west1-a',
        job_config=job_config
    )

job.result()
