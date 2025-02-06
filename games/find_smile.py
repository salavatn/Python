import random

class Colors:
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    DEFAULT = "\033[0m"


def calculate_counter() -> int: 
    """Расчитываем количество необходимых попыток"""
    count_to_win = 0
    count_numbers = 998

    while True:
        count_to_win += 1
        count_numbers = int(count_numbers / 2)
        if count_numbers == 0:
            return count_to_win


def main() -> None:
    """Выбирается рандомное число.
    Расчитывается сколько попыток использует пользователь
    Отображает какие были выбраны числа
    """
    print(f"\nВ диапазоне от 1 до 999 целых чисел скрывается smile '{Colors.YELLOW}☻{Colors.DEFAULT}' - найдите его номер!")

    count = calculate_counter()
    number = random.randint(1,999)
    attempt = 0
    number_list = []

    print(f"Cтань чемпионом! Угадай с {count} попытки!\n")

    print('Ваше число: ', end=' ')
    user_number = int(input())

    while True:
        attempt += 1
        if user_number == number:
            number_list.append(number)
            number_list.sort()
            if attempt <= count:
                print(f"\n\tПобедитель! Номер смайли {Colors.GREEN}☻{Colors.DEFAULT} = {number}")
                print(f"\tУгадал с {attempt} попытки!")
                print('\tВаши попытки: ', *number_list)
            else:
                print(f"\n\tНе плохо! Номер смайли {Colors.RED}☻{Colors.DEFAULT} = {number}")
                print(f"\n\tПссс... с {attempt} попытки и мой пёс справится")
            break
        else:
            number_list.append(number)
            number_list.append(user_number)
            number_list.sort()

            target_index = number_list.index(number)
            number_list[target_index] = f"{Colors.YELLOW}☻{Colors.DEFAULT}"

            print('Найдите номер смайли:', *number_list, '\n')
            number_list.remove(f"{Colors.YELLOW}☻{Colors.DEFAULT}")
            print('Ваше число: ', end=' ')
            user_number = int(input())


if __name__ == "__main__":
    main()