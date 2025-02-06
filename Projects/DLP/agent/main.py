import os
from time import time

keyword = "FactoryTestKeyWord"

file = '/Users/salavat/GitHub/Python/Projects/DLP/sampledata/example.txt'


time_start = time()
with open(file, 'r', encoding='UTF-8') as file:
    data = file.read()
    if keyword in data:
        print(keyword)
time_finish = time()

print(f'Result is {round(time_finish-time_start, 4)} sec')
