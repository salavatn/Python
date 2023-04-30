import os

current_dir = os.path.abspath(os.path.dirname(__file__))
print(f"Current dir: \t{current_dir}")

# Содержимое каталога
print(f"List dir: \t{os.listdir(current_dir)}")

# # Сожержимое файла
# file = open("database4.txt", "r")
# print(f"File content: \t{file.read()}")
# file.close()

# IP адрес
print(f"IP: \t\t{os.environ}")