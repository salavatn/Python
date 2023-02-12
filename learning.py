# Simple code for Python Threading
import threading

heart = ["♥", "♥♥♥", "♥♥♥♥♥", "♥♥♥♥♥♥♥", "♥♥♥♥♥♥♥♥♥"]
sun = ["☼", "☼☼☼", "☼☼☼☼☼", "☼☼☼☼☼☼☼", "☼☼☼☼☼☼☼☼☼"]
rhomb = ["♦", "♦♦♦", "♦♦♦♦♦", "♦♦♦♦♦♦♦", "♦♦♦♦♦♦♦♦♦"]
square = ["■", "■■■", "■■■■■", "■■■■■■■", "■■■■■■■■■"]
rectangles = ["█", "███", "█████", "███████", "█████████"]

def out_red(text):
    color = "\033[32m{}"
    print(color.format(text))
    print("\033[0m")

out_red("ПРИВЕТ")


def func_heart():
    for h in heart:
        name_thread = threading.current_thread().name
        print(name_thread, h)

def func_sun():
    for s in sun:
        name_thread = threading.current_thread().name
        print(name_thread, s)

def func_rhomb():
    for r in rhomb:
        name_thread = threading.current_thread().name
        print(name_thread, r)

def func_square():
    for s in square:
        name_thread = threading.current_thread().name
        print(name_thread, s)

def func_rectangles():
    for r in rectangles:
        print("Thread [  Base  ]\t", r)


threading_heart = threading.Thread(target=func_rhomb, name="Thread [ 1      ]\t")
threading_sun = threading.Thread(target=func_rhomb, name="Thread [   2    ]\t")
threading_rhomb = threading.Thread(target=func_rhomb, name="Thread [   3    ]\t")
threading_square = threading.Thread(target=func_rhomb, name="Thread [     4  ]\t")

threading_heart.start()
threading_sun.start()
threading_rhomb.start()
threading_square.start()

func_rectangles()