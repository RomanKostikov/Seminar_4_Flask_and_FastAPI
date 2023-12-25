# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import time
import threading
from random import randint


def get_sum(lst: list[int]):
    global total_sum
    lst_sum = 0

    for el in lst:
        lst_sum += el

    total_sum += lst_sum


total_sum: int = 0
main_list: list[int] = []
threads: list[threading.Thread] = []
start_time = time.time()

for _ in range(1000):
    new_list = [randint(1, 100) for _ in range(100)]
    thread = threading.Thread(target=get_sum, args=[new_list])
    main_list.extend(new_list)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(main_list)
print(f'{total_sum = }')
print(f'Done in {time.time() - start_time} seconds!')
# Done in 1.085019826889038 seconds!
