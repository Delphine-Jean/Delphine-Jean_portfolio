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
        self.dataset_id = "{}.project_crypto_etl".format(self.project)


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

    def get_table(self):
        pass


    def create_table(self):
        pass


    def delete_table(self):
        pass


    def load_json_from_gcs(self):
        pass

    def update_table(self):
        pass