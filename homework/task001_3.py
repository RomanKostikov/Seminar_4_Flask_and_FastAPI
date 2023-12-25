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
import asyncio
from random import randint

main_list: list[int] = []
total_sum: int = 0


async def get_sum(lst: list[int]):
    global total_sum
    lst_sum = 0

    for el in lst:
        lst_sum += el

    total_sum += lst_sum


async def main():
    global main_list
    tasks: list[asyncio.Task] = []

    for _ in range(1000):
        new_list = [randint(1, 100) for _ in range(1000)]
        task = asyncio.create_task(get_sum(new_list))
        main_list.extend(new_list)
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    start_time = time.time()
    print(main_list)
    print(f'{total_sum = }')
    print(f'Done in {time.time() - start_time} seconds!')

# Done in 0.09312152862548828 seconds!
