import logging
from local_logger import log_config
from logging.config import dictConfig

dictConfig(log_config)


def get_logger(logger_name: str = "app"):
    """
    Returns a logger for the given logger.
    By default logging will only work during web requests b/c of how it's configured
    for fastapi in main.py

    To start logging to /app/logs/app.log from any file, import this function.
    Usage:
    >>> from utils import get_logger
    >>> logger = get_logger()
    >>> logger.debug("Hello")

    From your localhost watch the logs from the /app/logs directory run `tail -f app.log`

    :param logger_name: Name of the logger to return as configured in local_logger.py
    :return: Logger object
    """
    logger = logging.getLogger(logger_name)
    return logger
