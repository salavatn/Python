from dotenv import load_dotenv
import os


# Section 1: Load .env file
load_dotenv(dotenv_path='.env')


# Section 2: Get environment variables
addr = os.getenv('CUSTOM_ADDRESS')
port = os.getenv('CUSTOM_PORT')
pswd = os.getenv('CUSTOM_PASSWORD')


# Section 3: Create data object
data = {
    'address':  addr,
    'port':     port,
    'password': pswd
}


# Section 4: Print data object
print(data)
