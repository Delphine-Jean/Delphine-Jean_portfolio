from flask import Flask
import logging
import os
from connectors import binance_client



logger = logging.getLogger()
logger.setLevel(logging.INFO)


stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s :: %(message)s")
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug("message is important only when dubugging")
logger.info("message for basic informations")
logger.warning("message to pay attention")
logger.error("message helps to debug an error")

def connection():
    api_secret_binance = os.getenv('api_secret')
    api_key_binance = os.getenv('api_key')
    binance = binance_client.BinancesClient(api_key_binance, api_secret_binance)
    historical_data = binance.get_historical_klines()
    market_depth = binance.get_market_depth()
    historical_trades = binance.get_historical_trades()
    return market_depth



if __name__ == '__main__':
    print(connection())