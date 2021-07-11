from google.cloud import bigquery
from google.oauth2 import service_account
import config
import json


class BigqueryClient:

    def __init__(self):
        self.client = bigquery.Client()
        self.project = self.client.project
        self.datasets = list(self.client.list_datasets())
        self.project = self.client.project
        self.dataset_id = None


    #datasets methods
    def check_dataset(self):

        if self.datasets:
            print('Dataset in project {}'.format(self.project))
            for data in self.datasets:
                print('\t{}'.format(data.dataset_id))
        else:
            print('{} project does not contain any datasets'.format(self.project))

    def create_dataset(self, new_dataset: str):
        self.new_data_set = new_dataset
        self.dataset_id = "{}.{}".format(self.project, self.new_data_set)

        self.dataset = bigquery.Dataset(self.dataset_id)
        self.dataset.location = "EU"

        self.dataset = self.client.create_dataset(self.dataset, timeout=30)  # Make an API request.
        print("Created dataset {}.{}".format(self.client.project, self.dataset.dataset_id))

    def delete_dataset(self, current_dataset_id: str):
        self.current_dataset_id = current_dataset_id
        self.dataset_id = "{}.{}".format(self.project, self.current_dataset_id)
        self.client.delete_dataset(self.dataset_id,delete_contents=True,not_found_ok=True)
        print("Dataset deleted{}".format(self.current_dataset_id))

    # tables methods


    def create_table(self, new_table: str, dataset:str):
        self.dataset = dataset
        self.new_table = new_table
        self.table_id = "{}.{}.{}".format(self.project, self.dataset, self.new_table)

        self.schema = [
            bigquery.SchemaField("open_time", "INTEGER"),
            bigquery.SchemaField("open", "FLOAT"),
            bigquery.SchemaField("high", "FLOAT"),
            bigquery.SchemaField("low", "FLOAT"),
            bigquery.SchemaField("close", "FLOAT"),
            bigquery.SchemaField("volume", "FLOAT"),
            bigquery.SchemaField("close_time", "INTEGER"),
            bigquery.SchemaField("quote_assets_volume", "FLOAT"),
            bigquery.SchemaField("number_trades", "INTEGER"),
            bigquery.SchemaField("taker_buy_base_asset_volume", "FLOAT"),
            bigquery.SchemaField("taker_buy_quote_asset_volume", "FLOAT"),
            bigquery.SchemaField("ignore", "FLOAT"),
        ]
        self.table = bigquery.Table(self.table_id, schema=self.schema)
        self.client.create_table(self.table_id, exists_ok=True, timeout=30)
        print(" Created table {}.{}.{}".format(self.table.project, self.table.dataset_id, self.table.table_id))

    def get_table(self):
        pass


    def delete_table(self):
        pass


    def load_json_from_gcs(self):
        return test

    def update_table(self):
        return test