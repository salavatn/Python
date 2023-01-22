import random


print("\nУкажите диапазон целых чисел, а ☻ скроется за одним из них.")
start = int(input("Начальное число: "))
finish = int(input('Финальное число: '))

number = random.randint(start,finish)

# Высчитываем сколько попыток необходимо
range = finish - start
count = 0
while True:
    count = count + 1
    range = int(range / 2)
    if range == 0:
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
            print(f"\n\tПобедитель! Номер смайли ☻ = {number}")
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
        number_list[target_index] = "☻"

        print('Найдите номер смайли:',*number_list, '\n')
        number_list.remove("☻")
        print('Ваше число: ', end=' ')
        user_number = int(input())
