from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from os import path
import os.path


def system_environment():
    os_environment_variables = dict(os.environ)
    environment_keys = os_environment_variables.keys()
    environment_keys = list(environment_keys)
    environment_keys = sorted(environment_keys)
    return [os_environment_variables, environment_keys]


def checking_file_env():
    check_file_env = path.exists(".env")
    return check_file_env


def add_custom_env_variables():
    env_variables = system_environment()[0]     # Environment Variables
    load_dotenv()                               # Add custom variables from .env file
    env_variables_updated = system_environment()[0]     # Environment Variables
    env_var_keys = system_environment()[1]      # Get all variables keys
    custom_env_var_dict = {}                         # Create clean dictionary
    for element in env_var_keys:                # Checking all variables keys
        if element not in env_variables:        # If element is not in variables - it's new element
            custom_env_var_dict[element] = env_variables_updated[element]      # Save new element like custom variables
    return custom_env_var_dict


def create_table(variable_keys, system_variables, table_name):
    print(f"Count of VAR:\t{variable_keys}")
    table_environment_variables = Table(title=f"\n\n{table_name}")
    table_environment_variables.add_column("Variable", justify="left")
    table_environment_variables.add_column("Value", justify="left")
    for key in variable_keys:
        value = str(system_variables[key])
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


def main():
    console = Console()
    system_environment_variables = system_environment()[0]
    system_variables_keywords = system_environment()[1]
    table_name = "System Environment Variables"
    table_sys_env_var = create_table(system_variables_keywords, system_environment_variables, table_name)
    console.print(table_sys_env_var)
    if checking_file_env() is True:
        table_name = "Custom Environment Variables"
        custom_variables_keywords = add_custom_env_variables()
        table_custom_env_var = create_table(custom_variables_keywords, system_environment_variables, table_name)
        console.print(table_custom_env_var)


main()



