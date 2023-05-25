numbers = list(map(int, input().split()))

count = len(numbers)

if count == 1:
    print(numbers[0])
    exit()

new_list = []
for id in range(count):
    left = numbers[id - 1]

    try:
        right = numbers[id + 1]
    except IndexError:
        right = numbers[0]

    new_list.append(left + right)

print(*new_list)
