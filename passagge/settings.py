from rich.console import Console
from rich.table import Table
from rich import box
import logging.config
import logging
import argparse

parser = argparse.ArgumentParser(description='Search products', prog='ppassage')
parser.add_argument('-t', '--title', type=str, help='Product title', required=False)
parser.add_argument('-c', '--color', type=str, help='Product color', required=False)
parser.add_argument('-s', '--size',  type=str, help='Product size',  required=False)
parser.add_argument('-p', '--price', type=str, help='Product price range', required=False)
parser.add_argument('-b', '--brand', type=str, help='Product brand',  required=False)
parser.add_argument('-sku', '--sku', type=str, help='Product SKU',   required=False)

# parser -f --fortmat [json, table]
parser.add_argument('-f', '--format', type=str, choices=['json', 'table'], help='Output format', default='table')

args = parser.parse_args()


logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


console = Console()
table = Table(title='Internet Market', box=box.ROUNDED)