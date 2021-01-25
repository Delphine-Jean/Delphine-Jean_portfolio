from google.cloud import storage
import pandas as pd
import urllib.request
from datetime import datetime
import json
from google.cloud import storage
#Requirement.txt
# pandas ==  1.2.1
#urllib3 ==  1.26.2
#google-cloud-storage

def extract_source():
    #timestamp of the current date 
    today = str(datetime.today().strftime('%Y-%m-%d-%Hh-%Mm-%Ss'))
    #API request to nomics API wit currencies dailies data
    url = "https://api.nomics.com/v1/currencies/ticker?key=d8db65ed1b68cdd651c4a08430daff3b&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&per-page=100&page=1"
    response = urllib.request.urlopen(url).read()
    #tranformation of the file in json 
    df = pd.read_json(response)
    result = df.to_json()
    parsed = json.loads(result)
    json.dumps(parsed, indent=4)
    file_json_extract = "extract-" + today +".json"

    #Import file inside Google Cloud Storage

    bucket_name='test-function-api'
    source_file_name= file_json_extract
    destination_blob_name='test.json'

    def upload_blob(bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name) 

        print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))
        upload_blob(bucket_name, source_file_name, destination_blob_name)


