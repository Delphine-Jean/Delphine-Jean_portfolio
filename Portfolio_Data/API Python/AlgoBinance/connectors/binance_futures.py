import logging  #library for the logs error / infos and debug
import time
import requests
from urllib.parse import urlencode #to encode string parameters
import hmac #library to encrypt data
import hashlib
import websocket #library to use data from websockets api
import threading  #library to run parallel functions
import typing
import ssl
import json

from models import * #data models for our dictionary apis data

logger = logging.getLogger()
#main class to get the api data from Binance
class BinanceClientFutures:

    def __init__(self, public_key: str, secret_key: str, testnet : bool):
        if testnet:
            self._base_url = "https://testnet.binancefuture.com"
        else:
            self._base_url = "https://fapi.binance.com"

        self._public_key = public_key
        self._secret_key = secret_key
        self._headers = {"X-MBX-APIKEY": self._public_key}
        self.contracts = self.get_contracts()
        self.balances = self.get_balance()
        self.prices = dict()
        self._ws_id = 1
        self._ws = None

        logger.info("Binance Futures Client successfully initialized")

    def _generate_signature(self, data: typing.Dict) -> str:
        return hmac.new(self._secret_key.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()



    def _make_request(self, method: str, endpoint: str, data: typing.Dict):

        if method == 'GET':
            try:
                response = requests.get(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None

        elif method == "POST":
            try:
                response = requests.post(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None
        elif method == "DELETE":
            try:
                response = requests.delete(self._base_url + endpoint, params=data, headers=self._headers)
            except Exception as e:
                logger.error("Connection error while making %s request to %s: %s", method, endpoint, e)
                return None
        else:
            raise ValueError()
        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)",
                         method, endpoint, response.json(),response.status_code)
            return None

    def get_contracts(self)  -> typing.Dict[str, Contract]:
        exchange_info = self._make_request("GET","/fapi/v1/exchangeInfo", dict())
        contracts = dict()
        if exchange_info is not None:
            for contract_data in exchange_info["symbols"]:
                contracts[contract_data["pair"]] = Contract(contract_data)
        return contracts

    def get_historical_candles(self, contract: Contract, interval: str) -> typing.List[Candle]:
        data = dict()
        data["symbol"] = contract.symbol
        data["interval"] = interval
        data["limit"] = 1000

        raw_candles = self._make_request("GET","/fapi/v1/klines", data)

        candles = []
        if raw_candles is not None:
            for c in raw_candles:
                candles.append(Candle(c))

        return candles


    def get_bids_ask(self, contract: Contract) -> typing.Dict[str, float]:
        data = dict()
        data["symbol"] = contract.symbol
        ob_data = self._make_request("GET", "/fapi/v1/ticker/bookTicker", data)

        if ob_data is not None:
            if contract.symbol not in self.prices:
                self.prices[contract.symbol] = {"bid" : float(ob_data["bidPrice"]), "ask": float(ob_data["askPrice"])}
            else:
                self.prices[contract.symbol]["bid"] = float(ob_data["bidPrice"])
                self.prices[contract.symbol]["ask"] = float(ob_data["askPrice"])

            return self.prices[contract.symbol]

    def get_balance(self) -> typing.Dict[str, Balance]:
        data = dict()
        data["timestamp"] = int(time.time() * 1000)
        data["signature"] = self._generate_signature(data)

        balances = dict()
        account_data = self._make_request("GET", "/fapi/v1/account", data)

        if account_data is not None:
            for a in account_data['assets']:
                balances[a['asset']] = Balance(a)

        return balances


    def place_order(self, contract: Contract, side:str, quantity: float,order_type: str, price=None, tif=None) -> OrderStatus:
        data = dict()
        data["symbol"] = contract.symbol
        data["side"] = side
        data["quantity"] = quantity
        data["type"] = order_type


        if price is not None:
            data["price"] = price

        if tif is not None:
            data['timeInForce'] = tif
        data["timestamp"] = int(time.time() * 1000)
        data["signature"] = self._generate_signature(data)

        order_status = self._make_request("POST","/fapi/v1/order", data)

        if order_status is not None:
            order_status = OrderStatus(order_status)

        return order_status

    def cancel_order(self, contract: Contract, orderId: int) -> OrderStatus:
        data = dict()
        data["orderId"] = orderId
        data["symbol"] = contract.symbol
        data["timestamp"] = int(time.time() * 1000)
        data["signature"] = self._generate_signature(data)

        order_status = self._make_request("DELETE", "/fapi/v1/order", data)

        if order_status is not None:
            order_status = OrderStatus(order_status)

        return order_status

    def get_order_status(self, contract: Contract, order_id: int) -> OrderStatus:
        data = dict()
        data["orderId"] = order_id
        data["symbol"] = contract.symbol
        data["timestamp"] = int(time.time() * 1000)
        data["signature"] = self._generate_signature(data)

        order_status = self._make_request("GET", "/fapi/v1/order", data)

        if order_status is not None:
            order_status = OrderStatus(order_status)

        return order_status

