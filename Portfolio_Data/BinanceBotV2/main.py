import logging
import tkinter as tk
from connectors.binance_futures import BinanceFuturesClient
import config

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
    binance = BinanceFuturesClient(config.API_KEY,
                                   config.API_SECRET, True)
    print(binance.get_balances())
    root = tk.Tk()
    root.mainloop()






