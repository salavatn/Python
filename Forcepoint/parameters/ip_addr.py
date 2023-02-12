import random


def get_ipaddress():
    last_octet = random.randint(100, 200)
    ipaddress = "172.30.3."
    return f'IPAddress "{ipaddress}{str(last_octet)}"'
