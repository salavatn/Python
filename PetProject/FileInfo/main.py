from FileInfo import GetInfo
from rich.table import Table
from rich.console import Console
from rich import box
import argparse
import os


def show_table():
    target = GetInfo(args.file)
    console = Console()
    table   = Table(show_header=True, header_style="bold magenta", box=box.SIMPLE) # box=box.ROUNDED)

    # Two columns with default justification (centered)
    table.add_column("Title", style="dim", width=12)
    table.add_column("Value")

    # Add a row for each info type
    table.add_row("File Path",  str(target.filepath))
    table.add_row("Size Bytes", str(target.get_size()['Size Bytes']))
    table.add_row("Size KB",    str(target.get_size()['Size Kilobytes']))
    table.add_row("Size MB",    str(target.get_size()['Size Megabytes']))
    table.add_row("Size GB",    str(target.get_size()['Size Gigabytes']))
    table.add_row("Created",    str(target.get_datetime()['File Created']))
    table.add_row("Modified",   str(target.get_datetime()['File Modified']))
    table.add_row("Accessed",   str(target.get_datetime()['File Accessed']))
    table.add_row("Extension",  str(target.get_filetype()['File Type']))
    table.add_row("Mime Type",  str(target.get_filetype()['Mime Type']))
    table.add_row("MD5 Hash",   str(target.get_hash()['MD5 Hash']))
    table.add_row("FQDN",       str(target.get_host_info()['FQDN']))
    table.add_row("IP Address", str(target.get_host_info()['IP Address']))

    console.print(table)

def show_json():
    target_file = GetInfo(args.file)
    print(target_file.get_datetime())
    print(target_file.get_size())
    print(target_file.get_filetype())
    print(target_file.get_hash())
    print(target_file.get_host_info())

parser = argparse.ArgumentParser(description='Get file info', prog='FileInfo')
parser.add_argument('file', metavar='file', type=str, help='File path')
parser.add_argument('-t', '--table', action='store_true', help='Show file info in table')
parser.add_argument('-j', '--json', action='store_true', help='Show file info in json')

args = parser.parse_args()

try:
    if args.table:  show_table()
    if args.json:   show_json()
except FileNotFoundError:
    print("File not found.")
    exit()

