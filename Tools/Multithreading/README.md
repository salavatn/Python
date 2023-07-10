# Multithreading

## Introduction
> Threading is a process of executing multiple threads simultaneously within a single process, which helps improve application performance. A thread is a lightweight process and the smallest unit of execution. On the other hand, multiprocessing involves executing multiple processes simultaneously in memory to enhance system performance. Processes are heavyweight and the largest units of execution. This article explores the differences between threading and multiprocessing in Python.

### 1. Threading
> Threading is the execution of multiple threads concurrently within a single process, aimed at improving application performance. Threads are lightweight processes and the smallest units of execution. They share process resources like memory and data, executing independently and making optimal use of the CPU. Threads are executed in memory and are typically used for small tasks, I/O operations, and CPU-bound tasks. They are designed for a single process, core, processor, memory space, address space, cache, code section, heap, stack, signal handler, file descriptor table, etc.

### 2. Multiprocessing
> Multiprocessing involves executing multiple processes simultaneously in memory to enhance system performance. Processes are heavyweight and the largest units of execution. Unlike threads, processes do not share process resources like memory and data. Each process executes independently, maximizing CPU utilization. Processes are executed in memory and are suitable for large tasks and CPU-bound operations. Similar to threads, processes are designed for a single process, core, processor, memory space, address space, cache, code section, heap, stack, signal handler, file descriptor table, etc.

### 3. Difference between Threading and Multiprocessing
> Threading allows the execution of multiple threads concurrently within a single process, resulting in improved application performance. Threads are lightweight processes that share process resources and are suitable for small tasks, I/O operations, and CPU-bound tasks. On the other hand, multiprocessing enables the execution of multiple independent processes simultaneously in memory, enhancing system performance. Processes are heavyweight and do not share process resources, making them suitable for large tasks and CPU-bound operations. Both threading and multiprocessing are designed for specific units of execution, such as processes, cores, processors, memory spaces, address spaces, caches, code sections, heaps, stacks, signal handlers, file descriptor tables, etc.

## Demo
```bash
$ python demo_visualize.py
```
```
1 Heart:        ♥
2 Rhombus:      ♦
3 Sun:          ☼
1 Heart:        ♥♥
2 Rhombus:      ♦♦
3 Sun:          ☼☼
1 Heart:        ♥♥♥
2 Rhombus:      ♦♦♦
3 Sun:          ☼☼☼
1 Heart:        ♥♥♥♥
2 Rhombus:      ♦♦♦♦
3 Sun:          ☼☼☼☼
1 Heart:        ♥♥♥♥♥
2 Rhombus:      ♦♦♦♦♦
3 Sun:          ☼☼☼☼☼
1 Heart:        ♥♥♥♥♥♥
2 Rhombus:      ♦♦♦♦♦♦
3 Sun:          ☼☼☼☼☼☼
1 Heart:        ♥♥♥♥♥♥♥
2 Rhombus:      ♦♦♦♦♦♦♦
3 Sun:          ☼☼☼☼☼☼☼
1 Heart:        ♥♥♥♥♥♥♥♥
2 Rhombus:      ♦♦♦♦♦♦♦♦
3 Sun:          ☼☼☼☼☼☼☼☼
```

--- 

```bash
$ python demo_stopwatch.py
```
```
██ 1 ██
██ 1 ██
...
    ██ 2 ██
    ██ 2 ██
...
        ██ 3 ██
        ██ 3 ██
...
            ██ 4 ██
            ██ 4 ██



██ 1 ██
                        ██ 4 ██
                ██ 3 ██
                ██ 3 ██
        ██ 2 ██
██ 1 ██
                        ██ 4 ██
                ██ 3 ██
                        ██ 4 ██
        ██ 2 ██
██ 1 ██
                ██ 3 ██
                        ██ 4 ██


Execute Directly:  0.681141 sec

Execute Threading: 0.243584 sec
```

## How to use
```python
from threading import Thread

def func():
    print("Hello World")

thread_func = Thread(target=func)
thread_func.start()
thread_func.join()
```
