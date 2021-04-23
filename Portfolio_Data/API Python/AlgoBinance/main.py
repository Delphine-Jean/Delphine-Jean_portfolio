import tkinter as tk
import logging
from connectors.binance_futures import BinanceClientFutures

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

if __name__ == '__main__':

    binance = BinanceClientFutures("XXXXXX",
                                   "XXXXXX",
                                   True)
    print(binance.get_contracts())
    root = tk.Tk()
    root.mainloop()






