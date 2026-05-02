""" 
logging builtin module
methods:
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
logging.getLogger(__name__) # create logger object
# Logger
logging.Logger.setLevel()
logging.Logger.addHandler()
logging.Logger.removeHandler()
logging.Logger.addFilter()
# Handler
logging.Handler.setLevel()
logging.Handler.setFormatter()

"""

import logging
# create logger object
logger = logging.getLogger(__file__)
logger.setLevel(level=logging.DEBUG)
# create a handler object
handler = logging.FileHandler("my.log")
# create a formatter object
formatter = logging.Formatter(
    fmt='%(asctime)s | %(levelname)s | %(name)s  | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# set the formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)
# output the log
logger.debug("Debug Log Message....")
logger.info("Info  Log Message....")
logger.error("Error Log Message....")
logger.critical("Critical Log Message....")
