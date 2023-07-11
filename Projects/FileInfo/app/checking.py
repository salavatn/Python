import os
# from config import logger

filepath = '/User/mark/file.txt'

file_exist = os.path.isfile(filepath)
if not file_exist:
    error_msg = f"File not found: {filepath}"
    print(error_msg)
    exit(1)

print('Hello World!')