import logging

LOG_FILENAME = "backend.log"
FORMAT = "[%(asctime)s - %(name)s - %(levelname)s]: %(message)s"

def get_log_handler(logger_name=""):
    logFormatter = logging.Formatter(FORMAT)

    logHandler = logging.FileHandler(f'{logger_name}.{LOG_FILENAME}')
    logHandler.setFormatter(logFormatter)
    logHandler.setLevel(logging.DEBUG)

    return logHandler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_log_handler(logger_name))
    return logger
