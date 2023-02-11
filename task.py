# data = [1, 3, 5, 6, 10]

data = input()
data = data.split()
data = [eval(i) for i in data]

new_data = []

data_len = len(data) - 1


for N in data:
    index = data.index(N)
    left_num = index - 1
    right_num = index + 1

    if index == data_len:
        left_num = index - 1
        right_num = 0
        result = int(data[left_num]) + int(data[right_num])
        new_data.append(result)
    elif data_len == 0:
        result = data[index]
        new_data.append(result)
    else:
        result = int(data[left_num]) + int(data[right_num])
        new_data.append(result)



print(*new_data)
