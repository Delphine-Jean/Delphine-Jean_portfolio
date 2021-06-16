import logging
from binance_client import BinanceAPI
from orders import Orders
import config
import time
from datetime import datetime, timedelta
from binance.client import Client
import datetime as dt
import pandas as pd
from bigquery_export_klines import BigqueryClient
from google.cloud import bigquery


import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


logging.debug('This a debug message')
logging.info('This a info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

if __name__ != '__main__':
    pass
else:

    def get_klines():

        binances = BinanceAPI(config.API_KEY, config.API_SECRET)

        response = binances.get_klines("BTCUSDT", "1m", startTime="06/01/2021 00:00:00", endTime="06/12/2021 00:00:00")
        data = pd.DataFrame(response)

        data.columns = ['open_time',
              'open', 'high', 'low', 'clsoe', 'volume',
              'close_time', 'quote asset volume', 'num_trades',
              'taker_base_vol', 'taker_quote_vol', 'ignore']

        data.to_json('./export.json', orient='index')
        print(data)

    get_klines()

    client = BigqueryClient()
    print(client.create_table("test","project_crypto_etl"))






















