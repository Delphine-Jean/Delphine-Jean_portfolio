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

    binance = BinanceClientFutures("7e450864b2670cc314f74dc9ee61597ca90bf33359cbf25a68d80e44b322ebe7",
                                   "7d91ab540e9aa25007cb7c2cf7b861c36eebb81850d7ccb9fa029890c4adad2c",
                                   True)
    print(binance.get_order_status("BTCUSDT", 2686399724))
    print(binance.cancel_order("BTCUSDT",2686399724))
    root = tk.Tk()
    root.mainloop()






