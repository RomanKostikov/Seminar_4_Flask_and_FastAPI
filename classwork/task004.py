# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import os
import threading
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent


def get_words_count(el: str):
    if os.path.isfile(os.path.join(BASE_DIR, el)):
        with open(os.path.join(BASE_DIR, el), encoding='utf-8') as f:
            words = 0
            for line in f:
                words += len(line.strip().split(' '))
            print(f'File: {el}, words: {words}')


threads: list[threading.Thread] = []

start_time = time.time()

for el in os.listdir(BASE_DIR):
    thread = threading.Thread(target=get_words_count, args=[el])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Completed work in {time.time() - start_time} seconds.')

# Вывод в консоль:
# Completed work in 0.002994060516357422 seconds.
