from binance.client import Client
import os

'''
        api_key_binance = os.getenv('api_key')
        api_secret_binance = os.getenv('api_secret')
'''


class BinancesClient:

    def __init__(self, api_key_binance, api_secret_binance):
        self._api_key_binance = api_key_binance
        self._api_secret_binance = api_secret_binance
        self.client = Client(api_key_binance, api_secret_binance)

    def get_contracts(self):
        pass

    def get_historical_candles(self):
        pass


    def get_historical_dates(self):
        pass

    def get_historical_klines(self):
        pass

    def get_balance(self):
        pass








