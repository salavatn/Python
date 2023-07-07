import socket
import time 
def check_connection(host, port):
    try:
        time.sleep(0.5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Connection to {host}:{port} successful")
        else:
            print(f"Connection to {host}:{port} failed")
        sock.close()
    
    except socket.error as e:
        print(f"Error occurred while checking connection: {e}")

host = 'https://google.com'
port = 80

check_connection(host, port)


for port in range(1, 100):
    check_connection(host, port)