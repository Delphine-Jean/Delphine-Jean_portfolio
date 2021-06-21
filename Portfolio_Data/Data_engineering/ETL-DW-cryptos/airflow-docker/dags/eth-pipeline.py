from  binance_client import *


def default_args():
    pass


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