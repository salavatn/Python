from threading import Thread, current_thread


# Section 1: Function with arguments
def print_msg(count):
    # Part 1: Get thread name
    thread_name = current_thread().name
    print(f'Thread name is {thread_name}')
    for i in range(count):    
        print('Hello Team')


# Section 2: Initialize threat with argument and name
thread = Thread(target=print_msg, args=(25,), name='Run 25 messages')


# Section 3: Start thread and wait for it to finish
thread.start()
thread.join()
