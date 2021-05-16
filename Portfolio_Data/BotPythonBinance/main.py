import tkinter as tk
import logging

logger = logging.getLogger()
logger.info("info message")
logger.debug("debug message")
logger.warning("warning message")
logger.error("error message")

logger.setLevel(logging.INFO
root = tk.Tk()

root.mainloop()

