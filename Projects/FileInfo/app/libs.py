# Libs: Logging
from colorlog import ColoredFormatter

import logging
import logging.config as log_config

from typing import List, Dict, Union, Any
import hashlib, mimetypes, math
import datetime, socket, os



# Section 1: Logging configuration
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('Demo')

import logging, logging.config #, colorlog
from rich.console import Console
from rich.table import Table
from rich import box
import argparse
import os