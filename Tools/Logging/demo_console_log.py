from colorlog import ColoredFormatter
import logging, logging.config


# Section 1: Logging configuration
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('Demo')


# Section 2: Logging examples
log_header = "Examples:"
message    = "this could be your Ad;"


# Section 3: Logging functions
logger.debug(f"{log_header} {message}")
logger.info(f"{log_header} {message}")
logger.warning(f"{log_header} {message}")
logger.error(f"{log_header} {message}")
logger.critical(f"{log_header} {message}")


# # Section 4: Logging with time to local file (log.txt)
# logger = logging.getLogger('Demo')
# logger.addHandler(logging.FileHandler('log.txt'))
# logger.info(f"{log_header} {message}")
