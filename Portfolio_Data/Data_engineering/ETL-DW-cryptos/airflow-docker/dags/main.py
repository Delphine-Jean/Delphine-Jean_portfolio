from  binance_client import *
import pandas as pd
import config

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


    # storing the data in JSON format
    data.to_json(r"C:\Users\delph\Documents\git\Jedha_bootcamp\Portfolio_Data\Data_engineering\ETL-DW-cryptos\airflow-docker\dags\files\export_klines.json", orient='index')

    # displaying the DataFrame
    print(data)

get_klines()