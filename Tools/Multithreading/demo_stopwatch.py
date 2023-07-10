from threading import Thread
from time import time, sleep


# Section 1: Functions for time testing
def counter_1():
    count = 0
    while count < 1000:
        sleep(0.0001)
        count += 1
        print(f'██ 1 ██')

def counter_2():
    count = 0
    while count < 1000:
        sleep(0.0001)
        count += 1
        print(f'\t██ 2 ██')

def counter_3():
    count = 0
    while count < 1000:
        sleep(0.0001)
        count += 1
        print(f'\t\t██ 3 ██')

def counter_4():
    count = 0
    while count < 1000:
        sleep(0.0001)
        count += 1
        print(f'\t\t\t██ 4 ██')


# Section 2: Execute functions directly and record time
start = time()
counter_1()
counter_2()
counter_3()
counter_4()
finish = time()
execution_directly = finish - start


sleep(1)


# Section 3: Instantiate threads
thread_1  = Thread(target=counter_1)
thread_2  = Thread(target=counter_2)
thread_3  = Thread(target=counter_3)
thread_4  = Thread(target=counter_4)


# Section 4: Execute functions in threads and record time
start = time()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
finish = time()
execution_thread = finish - start


# Section 5: Print results
print(f'\nExecute Directly:  {round(execution_directly, 6)} sec')
print(f'\nExecute Threading: {round(execution_thread, 6)} sec')