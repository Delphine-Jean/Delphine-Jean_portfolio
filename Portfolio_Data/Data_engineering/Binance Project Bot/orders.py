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

    def get_order_book(self):
        pass

    def get_order(self):
        pass

    def get_order_status(self):
        pass

    def get_ticker(self):
        pass

    def get_info(self):
        pass