import logging
import config
from binance_client import BinanceClient

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
    print(client.get_all_symbol_ticker("BTCUSDT"))




