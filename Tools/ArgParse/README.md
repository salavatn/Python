# Lib ArgParse

## Description
This is a simple example of how to use the argparse library in python.

## Usage
```bash
python demo.py -h
```
```
usage: demo.py [-h] --host HOST --port PORT --user USER --pswd PSWD

Demo arguments

options:
  -h, --help   show this help message and exit
  --host HOST  IP Address
  --port PORT  Port
  --user USER  Username
  --pswd PSWD  Password
```

---

```bash
python demo.py --host 192.168.100.12 --port 3389 --user Administrator --pswd Passw0rd
```
```
{'address': '192.168.100.12', 'port': 3389, 'username': 'Administrator', 'password': 'Passw0rd'}
```

