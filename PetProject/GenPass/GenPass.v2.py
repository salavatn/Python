import random
import argparse

parser = argparse.ArgumentParser(description='Generate passwords of specified length and complexity')
parser.add_argument('--length', help='length of the generated passwords', default=8, type=int,  )
parser.add_argument('--level',  help='complexity of the generated passwords', default='easy',choices=['easy', 'medium', 'hard'], )
parser.add_argument('--count',  help='number of passwords to generate',   default=1, type=int)
args = parser.parse_args()

def generator(length, level):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    num = '1234567890'
    sym = '!@#$%^&*()_+'

    if level == 'easy':
        type =  list(abc) + list(abc.upper())
    elif level == 'medium':
        type = list(abc) + list(num) + list(abc.upper())
    elif level == 'hard':
        type = list(abc) + list(sym) + list(num) + list(abc.upper())

    data = ''
    for i in range(length):
        symbol = random.choice(type)
        data  += str(symbol)
    return data

length_pswd = args.length  # 8-20
level_pswd  = args.level   # easy, medium, hard
count_pswd  = args.count    #get_count()   # 1-100

print('\nPassword List:')
while count_pswd > 0:
    count_pswd -= 1
    password = generator(length=length_pswd, level=level_pswd)
    print(f"  {password}")

print('\n')
