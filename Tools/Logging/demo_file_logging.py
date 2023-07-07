from colorlog import ColoredFormatter
import logging, logging.config


# Section 1: Logging configuration
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('Demo')


# Section 2: Add file handler to save logs to a file
file_handler = logging.FileHandler('output_log.txt')
logger.addHandler(file_handler)


# Section 3: Set custom log format
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)


# Section 3: Logging examples
log_header = "Examples:"
message = "this could be your Ad;"


# Section 4: Logging functions
logger.debug(f"{log_header} {message}")
logger.info(f"{log_header} {message}")
logger.warning(f"{log_header} {message}")
logger.error(f"{log_header} {message}")
logger.critical(f"{log_header} {message}")
