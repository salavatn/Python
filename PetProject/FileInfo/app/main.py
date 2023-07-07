from app.fileinfo import FileInfo
from app.config import console, table
from app.config import args


def show_table(file_path):
    file_properties = FileInfo(file_path)
    properties      = file_properties.get()

    # print(properties)

    for key in properties:

        # print(key, properties[key])
        table.add_row(key, properties[key])

    console.print(table)

# def show_json():
#     target_file = GetInfo(args.file)
#     print(target_file.get_datetime())
#     print(target_file.get_size())
#     print(target_file.get_filetype())
#     print(target_file.get_hash())
#     print(target_file.get_host_info())

filepath = args.file

if args.table:  
    show_table(filepath)

# try:
#     if args.table:  
#         show_table(filepath)
#     # if args.json:   show_json()
# except FileNotFoundError:
#     print("File not found.")
#     exit()

