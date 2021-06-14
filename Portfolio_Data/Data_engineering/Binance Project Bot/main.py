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


        """
    output of th klines requests example with labels
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "17928899.62484339" // Ignore.
  ]
]
        """
        print(data)

    get_klines()

    output = BigqueryClient()
    print(output)

















