import logging
from binance import BinanceAPI
from orders import Orders
import config
import time
from datetime import datetime, timedelta

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

if __name__ != '__main__':
    pass
else:
    binances = BinanceAPI(config.API_KEY,config.API_SECRET)


    response = binances.get_klines("BTCUSDT", "1h", startTime="01/01/2019 00:00:00", endTime="01/01/2021 00:00:00")

    print(response)












