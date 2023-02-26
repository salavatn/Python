from rich.console import Console
from rich.table import Table



# python ufanet.py --object A4 --name Box-214 --status done --description "Don't work"
# python ufanet.py --info "Box-214"

# python ufanet.py --obj A4 --name Box-214 --status done --descr "Don't work"


project = {
    "Б2": [{
        "box": "Шкаф-115",
        "description": "work finished",
        "status": "done"
    }],
}

value = project["Б2"][0]["box"]
element = "Box-214"
status = "done"

print("\x1b[41m    Hello")
table_name = Table(title="\n\nUfanet")
table_columns = ["  ",  "  А   ","  Б   ","  Г   ","  Д   ","  Е   ","  Ж   ","  И   ",
                "  К   ","  Л   ","  М   ","  Н   "]
table_data = [
                ["1", "", "", "", "", "[red]Ш-41"],
                ["2", "", "[green]Ш-115", "[green]114Г", "[green]112Г", " "],
                ["3", "[red]⬤[red]", "[yellow]⬤", "[green]⬤", "⬤", "⬤"],
                ["4", "[red] [  ]", "[red]🙫", "⬤", "⬤", "⬤"],
                ["5", "[red]🙩", "🙩", " ", " ", " "],
                ["6", " ", "[green]Ш-116", "[red]Ш-60\n[green]Ш-113", " ", " "],
                ["7", " ", " ", " ", " ", "[yellow]111Г", " ", "[red]102Г\n[yellow]27"],
                ["8", " ", " ", " ", " ", " "],
                ["9", f"{0x1F66B}", " ", " ", " ", " "],
                ["10", " ", " ", " ", " ", " "]
]


def get_table(table, columns, rows):
    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)


get_table(table_name, table_columns, table_data)

