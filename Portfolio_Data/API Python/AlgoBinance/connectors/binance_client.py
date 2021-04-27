from binance.client import Client

class BinancesClient:

    def __init__(self, api_key_binance, api_secret_binance):
        self._api_key_binance = api_key_binance
        self._api_secret_binance = api_secret_binance
        self.client = Client(api_key_binance, api_secret_binance)


    def get_market_depth(self):
        market_depth = self.client.get_order_book(symbol='ETHBTC')
        print(market_depth)

    def get_historical_klines(self):
        klines = self.client.get_historical_klines('ETHBTC', Client.KLINE_INTERVAL_30MINUTE, '30 MINUTES ago UTC' )
        return klines

    def get_historical_trades(self):
        agg_trades = self.client.aggregate_trade_iter(symbol="ETHBTC", start_str='30 minutes ago UTC')
        for trades in agg_trades:
            print(trades)







