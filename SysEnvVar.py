# System Environment Variables
from dotenv import load_dotenv
import os

load_dotenv()
os_env = dict(os.environ)

print(f"PY_MYSQL_ADDR: {os_env['PY_MYSQL_ADDR']}")
print(f"PY_MYSQL_USER: {os_env['PY_MYSQL_USER']}")
print(f"PY_MYSQL_PSWD: {os_env['PY_MYSQL_PSWD']}")
