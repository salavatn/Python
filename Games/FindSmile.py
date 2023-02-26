import random
import socket
hostname = socket.gethostname()


color_red = "\033[31m"
color_green = "\033[32m"
color_yellow = "\033[33m"
color_default = "\033[0m"


def game_condition(g_mode):
    if g_mode == "single":
        g_start = int(input("First number [1]: ") or 1)
        g_finish = int(input('Final number [100]: ') or 100)
        print(f"\nYour {hostname} selected the number and give it for the {color_yellow}Smile ☻{color_default}, find the number of {color_yellow}Smile{color_default}.")
        g_num = random.randint(g_start, g_finish)
        g_range = g_finish - g_start
        return [g_num, g_range]

    elif game_mode == "double":
        print(f"\nУкажите диапазон целых чисел, а {color_yellow}Smile ☻{color_default} скроется за одним из них.")


# Расчитываем количество необходимых попыток
game_mode = input("Hello, select mode [single/double]: ") or "single"
conditions = game_condition(game_mode)
game_range = conditions[1]
count = 0
while True:
    count = count + 1
    game_range = int(game_range / 2)
    if game_range == 0:
        print(f"Ты станешь чемпионом, если угадаешь с {count} попытки!\n")
        break

attempt = 0
number_list = []
print('Ваше число: ', end=' ')
user_number = int(input())

while True:
    attempt = attempt + 1
    if user_number == number:
        number_list.append(number)
        number_list.sort()
        if attempt <= count:
            print(f"\n\tПобедитель! Номер смайли {color_yellow}☻{color_default} = {number}")
            print(f"\tУгадал с {attempt} попытки!")
            print('\tВаши попытки: ', *number_list)
        else:
            print(f"\n\tХорошо, но с {attempt} попытки и мой пёс справится")
        break
    else:
        number_list.append(number)
        number_list.append(user_number)
        number_list.sort()

        target_index = number_list.index(number)
        number_list[target_index] = f"{color_yellow}☻{color_default}"

        print('Найдите номер смайли:', *number_list, '\n')
        number_list.remove(f"{color_yellow}☻{color_default}")
        print('Ваше число: ', end=' ')
        user_number = int(input())
