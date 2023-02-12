import time
import threading

time_start = time.time()

heart = ["♥", "♥♥♥", "♥♥♥♥♥", "♥♥♥♥♥♥♥", "♥♥♥♥♥♥♥♥♥"]
sun = ["☼", "☼☼☼", "☼☼☼☼☼", "☼☼☼☼☼☼☼", "☼☼☼☼☼☼☼☼☼"]
rhomb = ["♦", "♦♦♦", "♦♦♦♦♦", "♦♦♦♦♦♦♦", "♦♦♦♦♦♦♦♦♦"]
square = ["■", "■■■", "■■■■■", "■■■■■■■", "■■■■■■■■■"]
rectangles = ["█", "███", "█████", "███████", "█████████"]


def func_colors(color):
    if color == "black":
        return "\033[30m{}"
    elif color == "red":
        return "\033[31m{}"
    elif color == "green":
        return "\033[32m{}"
    elif color == "yellow":
        return "\033[33m{}"
    elif color == "blue":
        return "\033[34m{}"
    elif color == "purple":
        return "\033[35m{}"
    elif color == "turquoise":
        return "\033[36m{}"
    elif color == "white":
        return "\033[37m{}"


def func_symbols(symbols, color):
    for symbol in symbols:
        time.sleep(0.1)
        selected_color = func_colors(color)
        default_color = "\033[0m{}"
        thread_name = threading.current_thread().name
        print(thread_name, selected_color.format(symbol), default_color.format(""))


threading_1 = threading.Thread(target=func_symbols, args=(heart, "red"), name="Thread [1       ]\t")
threading_2 = threading.Thread(target=func_symbols, args=(rhomb, "green"), name="Thread [ 2      ]\t")
threading_3 = threading.Thread(target=func_symbols, args=(sun, "blue"), name="Thread [  3     ]\t")
threading_4 = threading.Thread(target=func_symbols, args=(heart, "white"), name="Thread [   4    ]\t")
threading_5 = threading.Thread(target=func_symbols, args=(square, "purple"), name="Thread [    5   ]\t")
threading_6 = threading.Thread(target=func_symbols, args=(sun, "red"), name="Thread [     6  ]\t")
threading_7 = threading.Thread(target=func_symbols, args=(rectangles, "yellow"), name="Thread [      7 ]\t")
threading_8 = threading.Thread(target=func_symbols, args=(rhomb, "turquoise"), name="Thread [       8]\t")

threading_1.start()
threading_2.start()
threading_3.start()
threading_4.start()
threading_5.start()
threading_6.start()
threading_7.start()
threading_8.start()

threading_1.join()
threading_2.join()
threading_3.join()
threading_4.join()
threading_5.join()
threading_6.join()
threading_7.join()
threading_8.join()

time_finish = time.time()

print(f"\nTime for processing is: {round(time_finish-time_start, 4)} second \n\n")