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
import multiprocessing
from random import randint


def get_sum(lst: list[int], cnt: multiprocessing.Value):
    lst_sum = 0

    for el in lst:
        lst_sum += el

    with cnt.get_lock():
        cnt.value += lst_sum


def main():
    total_sum = multiprocessing.Value('i', 0)
    main_list: list[int] = []
    processes: list[multiprocessing.Process] = []

    for _ in range(1000):
        new_list = [randint(1, 100) for _ in range(1000)]
        process = multiprocessing.Process(
            target=get_sum, args=(new_list, total_sum)
        )
        main_list.extend(new_list)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(main_list)

    return total_sum


if __name__ == '__main__':
    start_time = time.time()
    res = main()

    with res.get_lock():
        total_sum = res.value

    print(f'{total_sum = }')
    print(f'Done in {time.time() - start_time} seconds!')
# Done in 81.35060834884644 seconds!
