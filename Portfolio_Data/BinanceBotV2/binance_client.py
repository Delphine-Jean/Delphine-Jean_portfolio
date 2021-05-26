from binance.client import Client
from binance.enums import *
from binance.exceptions import *



class BinanceClient:
    def __init__(self, api_key : str, secret_api : str, testnet : bool):
        self.api_key = api_key
        self.secret_api = secret_api
        self.testnet = testnet
        self.client = Client(self.api_key, self.secret_api, testnet=self.testnet)


    def get_client(self):
        return self.client


    def get_all_symbol_ticker(self, symbol=None):
        self.symbol = symbol
        prices = self.client.get_all_tickers(self.symbol)
        if prices is not None:
            for price in prices:
                print(price)

    def get_symbol_historical_ticker_candles(self, symbol: str, interval, start_str : str, end_str=None):
        self.symbol = symbol
        self.interval = interval
        self.start_str = start_str
        self.end_str = end_str

        data = self.client.get_historical_klines(self.symbol,self.interval ,self.start_str, self.end_str )

        if data is not None:
            for datas in data:
                print(datas)



    def create_order(self, symbol,side,type,timeInForce, quantity, price):
        self.symbol = symbol
        self.side = side
        self.type = type
        self.timeInForce = timeInForce
        self.quantity = quantity
        self.price = price

        order = self.client.create_test_order(self.symbol,
            self.side,
            self.type,
            self.timeInForce,
            self.quantity,
            self.price)

        for orders in order:
            print(order)

    def get_order(self):
        pass

    def cancel_order(self):
        pass






"""
class Binance
api key
secret key

method : get client(api_key, secret_key)
return response

method get symbol ()
asset + symbol

method get_symbol_ticker(symbol)
client.get_symbol_ticker(symbol, interval)

method historical_symbol_ticker_candles()
client.get_historical_symbol_tickers_candles(symbol, interval, period)

method asset_balance()
client.get_asset_balance(asset)
method order()
client.create_order_market_buy(symbol, quantiy)
client.create_order_market_sell(symbol, quantity)

method get_order(symbol,id_order)

method cancel_order(symbol, id_order)

"""
