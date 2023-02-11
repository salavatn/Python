import datetime
import socket
import os


hostname = socket.getfqdn()     # DESKTOP-4UL675L.home
ip_address = socket.gethostbyname(hostname)



path = r"C:\tmp\file597-UTF-8.txt"
path2 = r"C:\Users\admin\Downloads\ubuntu-22.04.1-desktop-amd64.iso"


def get_file_date_info(filepath):
    file = os.stat(path2)
    created = datetime.datetime.fromtimestamp(file.st_ctime)
    modified = datetime.datetime.fromtimestamp(file.st_mtime)
    accessed = datetime.datetime.fromtimestamp(file.st_atime)
    result = {
        "file created": str(created),
        "file modified": str(modified),
        "file accessed": str(accessed),
        "file size": str(file_size)
        }
    return result

file_status = os.stat(path2)

def get_file_size_info(file_status):
    get_all = os.stat(path2)
    size = get_all.st_size
    file_size = None
    for volume in ['Bytes', 'KB', 'MB', 'GB']:
        if size < 1024:
            file_size = f"{round(size, 2)} {volume}"
            break
        else:
            size /= 1024
    result = {"file size": str(file_size)}
    return result
# INSIDE: r"C:\Users\admin\Downloads\ubuntu-22.04.1-desktop-amd64.iso"
# OUTSIDE: {'file size': '3.56 GB'}

print(get_file_date_info(path))


print(f"FQDN:\t\t{hostname}")
print(f"IP Addr: \t{ip_address}")

file_info(path2)