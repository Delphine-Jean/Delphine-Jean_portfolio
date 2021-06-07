import config
from binance import BinanceAPI

client = BinanceAPI(config.API_KEY, config.API_SECRET)

class Orders:

    def buy_limit(self, symbol, quantity, buyPrcie):

        order = client.buy_limit(symbol, quantity, buyPrcie)

        if order is not None:
            return order

    def sell_limit(self, symbol, quantity, sellPrice):

        order = client.sell_limit(symbol, quantity, sellPrice)

        if order is not None:
            return order

    def buy_market(self, symbol, quantity):

        order = client.buy_market(symbol, quantity)

        if order is not None:
            return order

    def sell_market(self, symbol, quantity):

        order = client.sell_market(symbol, quantity)

        if order is not None:
            return order

    def cancel_order(self, symbol, orderId):

        order = client.cancel(symbol, orderId)

        return order['status']

    def get_order_book(self, symbol, limit):

        order = client.get_order_books(symbol,limit)

        return order

    def get_order(self, symbol, orderId):
        order = client.query_order(symbol, orderId)

        if order is not None:
            return order

    def get_order_status(self, symbol, orderId):
        order = client.query_order(symbol, orderId)

        if order is not None:
            return order["status"]

    def get_ticker(self, symbol):
        ticker = client.get_ticker(symbol)
        return ticker


    def get_info(self):
        info = client.get_exchange_info()
        print(info)