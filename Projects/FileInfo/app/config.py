import logging, logging.config #, colorlog
from rich.console import Console
from rich.table import Table
from rich import box
import argparse, os


# Config-1: Logging 
logging.config.fileConfig('logging.conf')
logger = logging


# Config-2: Argument Parser
if __name__ == "app.config":
    argparser = argparse.ArgumentParser(description='Get file info')
    argparser.add_argument('--file',  type=str,            help='File path')
    argparser.add_argument('--table', action='store_true', help='Show file info in table')
    argparser.add_argument('--json',  action='store_true', help='Show file info in json')
    args = argparser.parse_args()


# Config-3: Console and Table
console = Console(color_system="truecolor")
table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE)
table.add_column("Title", style="dim", width=13)
table.add_column("Value")

