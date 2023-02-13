from rich.console import Console
from rich.table import Table

table_src_args = Table(title="\nSource Arguments")
col_src_args = ["ID", "Type", "Random Value", "Specific Value", "Example"]
row_src_args = [
    ["1", "IP Address",     "-src ip:*", "172.30.1.22",      "-src ip:172.30.1.22"],
    ["2", "Hostname",       "-src host:*", "workstation",      "-src host:workstation"],
    ["3", "Email Address",  "-src email:*", "user@corp.com",    "-src email:user@corp.com"],
    ["4", "User Name",      "-src user:*", "Tim Muller",    "-src user:'Tim Muller'"]
]


table_dst_args = Table(title="\nDestination Arguments")
col_dst_args = ["ID", "Destination Type", "Random Value", "Specific Value", "Example"]
row_dst_args = [
    ["1", "LAN",                "-src lan:*", "FileServer",         "-src 1:FileServer"],
    ["2", "Removable Media",    "-src usb:*", "SDcard",             "-src 2:SDcard"],
    ["3", "Endpoint Printing",  "-src printer:*", "HP_LaserJet",    "-src 3:HP_LaserJet"],
    ["4", "URL address",        "-src url:*", "dropbox.com",        "-src 4:dropbox.com"],
    ["5", "Email Address",      "-src email:*", "friend@gmail.com", "-src 6:friend@gmail.com"]
]

table_sid_args = Table(title="\nDestination Arguments")
col_sid_args = ["ID", "Destination Type", "Random Value", "Specific Value", "Example"]
row_sid_args = [
    ["1", "LAN",                "-src 1:*", "FileServer",       "-src 1:FileServer"],
    ["2", "Removable Media",    "-src 2:*", "SDcard",           "-src 2:SDcard"],
    ["3", "Endpoint Printing",  "-src 3:*", "HP_LaserJet",      "-src 3:HP_LaserJet"],
    ["4", "Endpoint HTTP",      "-src 4:*", "webfile.org",      "-src 4:webfile.org"],
    ["5", "Endpoint HTTPS",     "-src 5:*", "dropbox.com",      "-src 5:dropbox.com"],
    ["6", "Email Address",      "-src 6:*", "friend@gmail.com", "-src 6:friend@gmail.com"],
]


def get_table(table, columns, rows):
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)


get_table(table_src_args, col_src_args, row_src_args)

get_table(table_dst_args, col_dst_args, row_dst_args)
