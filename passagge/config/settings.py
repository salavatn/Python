from typing import List, Dict, Union, Optional, Any, Tuple, Callable, TypeVar, Generic, Deque, Type, Set, cast, no_type_check, AnyStr
from rich.console import Console
from rich.table import Table
from rich import box
import logging.config
import logging
import argparse
import locale
import re

parser = argparse.ArgumentParser(description='Search products', prog='ppassage')
parser.add_argument('--title',    type=str, help='Product title',    default='джинсы')
parser.add_argument('--sku',      type=str, help='Product SKU',      )
parser.add_argument('--color',    type=str, help='Product color',    )
parser.add_argument('--brand',    type=str, help='Product brand',    )
parser.add_argument('--type',     type=str, help='Product type',     )
parser.add_argument('--category', type=str, help='Product category', )
parser.add_argument('--country',  type=str, help='Product country',  )
parser.add_argument('--price',    type=str, help='Product price',    )
parser.add_argument('--size',     type=str, help='Product size',    choices=['show', 'hide'],  default='hide')
parser.add_argument('--output',   type=str, help='Output format',   choices=['json', 'table'], default='table')
parser.add_argument('--limit',    type=str, help='Show limit count',choices=['one', 'all'],    default='10')


args = parser.parse_args()


logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger()


console = Console()
table = Table(title='Internet Market', box=box.ROUNDED)


