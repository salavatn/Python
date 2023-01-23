import re
import os
import filetype

    # pathUser      - Пользователь вводит путь C:\Users\admin\Documents
    # pathChecking  - Если в конце нет "\", то добавляем
    # pathEscaped   - Конвертация в "C:\\Users\\admin"

pathUser = input('Enter Folder path: ')
pathChecking = list(pathUser)
if pathChecking[-1] != '\\':
    pathUser = pathUser + '\\'
pathEscaped = re.escape(pathUser)

    # fileInfo      - Словарь, содержащий информацию о файле
fileTypeParentKeys = ['fileName', 'fileProperties']
fileTypeChildKeys = ['fileExtention', 'fileMIME', 'fileSize', 'filePath']
fileInfo = dict.fromkeys(fileTypeParentKeys)
fileInfo['fileProperties'] = dict.fromkeys(fileTypeChildKeys)
print(fileInfo)


    # Сканируем каталог и возвращаем список всех файлов
def ScanningFolder(path):
    list_files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            list_files.append(i)
    return list_files


    # C:\Users\admin\Documents\ + Document.pdf'
def FileFullPath(path, file):
    pathFile = path + file
    return pathFile

    # Возвращаем тип файла. PDF
def FileTypeExtention(fileFullPath):
    kind = filetype.guess(fileFullPath)
    if kind is None:
        print('Not defined')
        return
    return(kind.extension)

    # Возвращаем MIME файла. application/pdf
def FileTypeMIME(fileFullPath):
    kind = filetype.guess(fileFullPath)
    if kind is None:
        print('Not defined')
        return
    return (kind.mime)


    # files     - Полный путь до конечного файла
files = ScanningFolder(pathEscaped)

    # fileInfo  - Записываем свойства файла: Name, Extension, MIME, Size, Path
for file in files:
    pathFile = (FileFullPath(pathUser, file))
    fileInfo['fileName'] = file
    fileInfo['fileProperties']['filePath'] = pathFile
    fileInfo['fileProperties']['fileExtention'] = FileTypeExtention(pathFile)
    fileInfo['fileProperties']['fileMIME'] = FileTypeMIME(pathFile)
    print(fileInfo)
