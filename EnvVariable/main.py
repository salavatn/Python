from rich.console import Console
from rich.table import Table
import os


def system_environment():
    os_enviroment_variables = dict(os.environ)
    environment_keys = os_enviroment_variables.keys()
    environment_keys = list(environment_keys)
    environment_keys = sorted(environment_keys)
    return [os_enviroment_variables, environment_keys]


def create_table(variable_keys, system_environment):
    table_environment_variables = Table(title="\n\nEnvironment Variables")
    table_environment_variables.add_column("Variable", justify="left")
    table_environment_variables.add_column("Value", justify="left")
    for key in variable_keys:
        value = str(system_environment[key])
        if key == "PS1":
            table_environment_variables.add_row(key, value)
        elif ":" in value:
            value = value.replace(":", " ")
            value = value.split()
            value_full = ""
            value_part = ""
            for el_value in value:
                value_part += el_value
                value_part += ",\t"
                if len(value_part) >= 70:
                    value_part += "\n"
                    value_full += value_part
                    value_part = ""
            value = value_full
        table_environment_variables.add_row(key, value)
    return table_environment_variables


sys_var = system_environment()[0]
sys_var_keys = system_environment()[1]
table = create_table(sys_var_keys, sys_var)

console = Console()
console.print(table)

