import logging
import config
from binance_client import BinanceClient
from binance.client import Client
from binance.enums import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)


logging.debug('This a debug message')
logging.info('This a info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)


if __name__ == '__main__':


    client = BinanceClient(
        api_key= config.API_KEY,
        secret_api=config.API_SECRET,
        testnet = True)
    interval = Client.KLINE_INTERVAL_1MINUTE


    """print(client.create_order(
        symbol='BNBBTC',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity =100,
        price='0.00001'
    ))"""

    print(client.get_all_symbol_ticker())



