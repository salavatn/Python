import logging
import logging.config
from colorlog import ColoredFormatter


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def get_info():
    log_header = "get_info"
    message    = "Today we will learn about Logging in Python"

    logger.info(f"{log_header}: {message}")



def log_examples():
    log_header = "log_examples"
    message    = "this could be your Ad"

    logger.debug(f"{log_header}: {message}")
    logger.info(f"{log_header}: {message}")
    logger.warning(f"{log_header}: {message}")
    logger.error(f"{log_header}: {message}")
    logger.critical(f"{log_header}: {message}")

