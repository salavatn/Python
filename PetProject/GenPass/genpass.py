import random

def get_length():
    while True:
        length = int(input('Укажите длину пароля(8-20):\t' ))
        if length in range(8, 21):
            return length
    
def get_level():
    return input('Cложность (easy, medium, hard):\t')

def get_count():
    while True:
        count = int(input('Укажите колличество паролей:\t'))
        if count > 0:
            return count

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

length_pswd = get_length()  # 8-20
level_pswd  = get_level()   # easy, medium, hard
count_pswd  = get_count()   # 1-100

print('\nПароли:')
while count_pswd > 0:
    count_pswd -= 1
    password = generator(length=length_pswd, level=level_pswd)
    print(f"  {password}")

print('\n')
