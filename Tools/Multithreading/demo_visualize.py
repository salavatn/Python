from threading import Thread
from time import sleep


# Section 1: Functions to be executed in threads
def heart():
    for i in range(1, 9):
        print(f'1 Heart:\t{"♥" * i}')
        sleep(0.0001)

def rhombus():
    for i in range(1, 9):
        print(f'2 Rhombus:\t{"♦" * i}')
        sleep(0.0001)

def sun():
    for i in range(1, 9):
        print(f'3 Sun:\t\t{"☼" * i}')
        sleep(0.0001)


# Section 2: Instantiate threads
thread_heart   = Thread(target=heart)
thread_rhombus = Thread(target=rhombus)
thread_sun     = Thread(target=sun)


# Section 3: Start threads
thread_heart.start()
thread_rhombus.start()
thread_sun.start()


# Section 4: Wait for threads to finish
thread_heart.join()
thread_rhombus.join()
thread_sun.join()


# Output example:
# 1 Heart:        ♥
# 2 Rhombus:      ♦
# 3 Sun:          ☼
# 1 Heart:        ♥♥
# 2 Rhombus:      ♦♦
# 3 Sun:          ☼☼
# 1 Heart:        ♥♥♥
# 2 Rhombus:      ♦♦♦
# 3 Sun:          ☼☼☼
# 1 Heart:        ♥♥♥♥
# 2 Rhombus:      ♦♦♦♦
# 1 Heart:        ♥♥♥♥♥
# 3 Sun:          ☼☼☼☼
# 2 Rhombus:      ♦♦♦♦♦
# 1 Heart:        ♥♥♥♥♥♥
# 3 Sun:          ☼☼☼☼☼
# 2 Rhombus:      ♦♦♦♦♦♦
# 1 Heart:        ♥♥♥♥♥♥♥
# 3 Sun:          ☼☼☼☼☼☼
# 2 Rhombus:      ♦♦♦♦♦♦♦
# 1 Heart:        ♥♥♥♥♥♥♥♥
# 3 Sun:          ☼☼☼☼☼☼☼
# 2 Rhombus:      ♦♦♦♦♦♦♦♦
# 3 Sun:          ☼☼☼☼☼☼☼☼