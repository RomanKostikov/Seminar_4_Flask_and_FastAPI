# Задание №5
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.

import os
import multiprocessing
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent


def get_words_count(el: str):
    if os.path.isfile(os.path.join(BASE_DIR, el)):
        with open(os.path.join(BASE_DIR, el), encoding='utf-8') as f:
            words = 0
            for line in f:
                words += len(line.strip().split())
            print(f'File: {el}, words: {words}')


processes: list[multiprocessing.Process] = []

if __name__ == "__main__":
    start_time = time.time()

    for el in os.listdir(BASE_DIR):
        process = multiprocessing.Process(target=get_words_count, args=[el])
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Completed work in {time.time() - start_time} seconds.')

# Вывод в консоль:
# Completed work in 0.2418200969696045 seconds.
