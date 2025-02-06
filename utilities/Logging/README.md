# Lib logging

## Description
> This library is used to log messages to the console and to a file.

## Usage
1. To use this library, you must first import it into your project.
    ```python
    import logging, logging.config
    ```
2. Then you need to configure the logger.
    ```python
    logging.config.fileConfig('logging.conf')
    ```
3. Now you can use the logger.
    ```python
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    ```
4. The output will be as follows:
    ```bash
    2019-12-04 15:51:01,000 - DEBUG - This is a debug message
    2019-12-04 15:51:01,000 - INFO - This is an info message
    2019-12-04 15:51:01,000 - WARNING - This is a warning message
    2019-12-04 15:51:01,000 - ERROR - This is an error message
    2019-12-04 15:51:01,000 - CRITICAL - This is a critical message
    ```

## Configuration
> The configuration file is called `logging.conf` and is located in the root directory of the project.
```
[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=defaultFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=defaultFormatter
args=(sys.stdout,)

[formatter_defaultFormatter]
class=colorlog.ColoredFormatter
format=%(asctime)s - %(name)s - %(log_color)s%(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```
