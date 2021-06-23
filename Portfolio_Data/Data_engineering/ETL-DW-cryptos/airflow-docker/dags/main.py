from  binance_client import *
import pandas as pd
import config
import datetime
import os
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def default_args():
    pass


def get_klines():
    binances = BinanceAPI(config.API_KEY, config.API_SECRET)


    response = binances.get_klines("BTCUSDT", "1m", startTime="06/01/2021 00:00:00", endTime="06/12/2021 00:00:00")
    data = pd.DataFrame(response)

    data.columns = ['open_time',
              'open', 'high', 'low', 'close', 'volume',
              'close_time', 'quote asset volume', 'num_trades',
              'taker_base_vol', 'taker_quote_vol', 'ignore']

    data.open_time = pd.to_datetime(data.open_time, unit='ms')
    data.close_time = pd.to_datetime(data.close_time, unit='ms')
    data.set_index('open_time', inplace=True)
    # storing the data in CSV format
    current_date = datetime.datetime.now()
    filename = str(current_date.day) + str(current_date.month) + str(current_date.year)
    current_path = os.getcwd()
    data.to_csv(str(current_path) + r"\files\export_klines" + str(filename + "_.csv"))

    # displaying the DataFrame
    print(data)



get_klines()