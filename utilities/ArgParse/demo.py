from argparse import ArgumentParser


# Section 1: Create instance of ArgumentParser
parser = ArgumentParser(description='Demo arguments')


# Section 2: Add arguments
parser.add_argument('--host', type=str, required=True, help='IP Address')
parser.add_argument('--port', type=int, required=True, help='Port')
parser.add_argument('--user', type=str, required=True, help='Username')
parser.add_argument('--pswd', type=str, required=True, help='Password')


# Section 3: Parse arguments
args = parser.parse_args()
address  = args.host
port     = args.port
username = args.user
password = args.pswd


# Section 4: Create dictionary and print
data = {
    'address': address,
    'port': port,
    'username': username,
    'password': password
}

print(data)