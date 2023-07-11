from libs import Console, Table, box
from libs import argparse
from libs import logging, log_config


# Section 1: Logging configuration
log_config.fileConfig('logging.conf')
logger = logging


# Section 2: Argument parser
parser = argparse.ArgumentParser(description='Get file properties')
parser.add_argument('--file',  type=str,            help='File path')
parser.add_argument('--table', action='store_true', help='Show file info in table')
parser.add_argument('--json',  action='store_true', help='Show file info in json')
args = parser.parse_args()


# Section 3: Console table
console = Console(color_system="truecolor")
table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
table.add_column("Title", style="dim", width=13)
table.add_column("Value")
