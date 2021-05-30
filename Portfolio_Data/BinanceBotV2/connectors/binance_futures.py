import logging
import requests
import pprint
import time
import hmac
import hashlib
from urllib.parse import urlencode

logger = logging.getLogger()

"""
Some endpoints will require an API Key. Please refer to this page
The base endpoint is: https://fapi.binance.com
All endpoints return either a JSON object or array.
Data is returned in ascending order. Oldest first, newest last.
All time and timestamp related fields are in milliseconds.
"""
# base REST url
"https://fapi.binance.com"
"https://testnet.binancefuture.com"

# websocket
"wss://stream.binancefuture.com"


class BinanceFuturesClient:
    def __init__(self, public_key, secret_key, testnet):
        if testnet:
            self.base_url = "https://testnet.binance.vision/api"
            self.wss_url = "wss://stream.binance.com:9443/ws"
        else:
            self.base_url = "https://api.binance.com"
            self.wss_url = "wss://testnet.binance.vision/ws"

        self.prices = dict()

        self.public_key = public_key
        self.secret_key = secret_key

    def get_headers(self):
        headers = {
            'Accept': 'application/json'
        }

        if self.public_key:
            assert self.public_key
            headers['X-MBX-APIKEY'] = self.public_key


    def generate_signature(self, data):
        return hmac.new(self.secret_key.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()

    def make_request(self, method, endpoint, data):
        if method == "GET":
            response = requests.get(self.base_url + endpoint, params=data)
        else:
            raise ValueError()
        if response.status_code == 200:
            return response.json()
        else:
            logger.error('Error whle making %s request to %s : %s (error code %s)',
                         method, endpoint, response.json, response.status_code)
            return None

    def get_contracts(self):
        exchange_info = self.make_request("GET", "/fapi/v1/exchangeInfo", None)

        contracts = dict()
        if exchange_info is not None:
            for contract_data in exchange_info['symbols']:
                contracts[contract_data['pair']] = contract_data
        return contracts

    def get_historical_candles(self, symbol, interval):
        data = dict()
        "GET /fapi/v1/klines"
        data['symbol'] = symbol
        data['interval'] = interval
        data['limit'] = 1000

        raw_candles = self.make_request("GET", "/fapi/v1/klines", data)

        candles = []

        if raw_candles is not None:
            for candle in raw_candles:
                candles.append([candle[0], float(candle[1]), float(candle[1]), float(candle[2]), float(candle[3]),
                                float(candle[4]), float(candle[5])])

        return candles

    def get_bid_ask(self, symbol):
        data = dict()
        data['symbol'] = symbol

        ob_data = self.make_request("GET", "/fapi/v1/ticker/bookTicker", data)
        if ob_data is not None:
            if symbol not in self.prices:
                self.prices[symbol] = {"bid": float(ob_data['bidPrice']), 'ask': float(ob_data['askPrice'])}

            else:
                self.prices[symbol]['bid'] = float(ob_data['bidPrice'])
                self.prices[symbol]['ask'] = float(ob_data['askPrice'])

        return self.prices[symbol]

    def get_balances(self):
        data = dict()
        data['timestamp'] = int(time.time() * 1000)
        data['signature'] = self.generate_signature(data)

        balances = dict()

        account_data = self.make_request('GET', '/fapi/v2/account', data)

        if account_data is not None:
            for a in account_data["assets"]:
                balances[a["asset"]] = a

        return balances

    def place_order(self):
        return

    def cancel_order(self):
        return

    def get_order_status(self, symbol, order_id):
        data = dict()
        data['timestamp'] = int(time.time() * 1000)
        data['symbol'] = symbol
        data['orderId'] = order_id
        data['signature'] = self.generate_signature(data)

        order_status = self.make_request('GET', '/fapi/v1/order', data)

        return order_status
