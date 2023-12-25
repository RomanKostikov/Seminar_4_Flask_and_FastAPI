# Задание №2
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте процессы.

import os
import multiprocessing
from pathlib import Path
import time
import requests

BASE_DIR = Path(__file__).resolve().parent
saves_dir = os.path.join(BASE_DIR, 'saves_2')

if not os.path.exists(saves_dir):
    os.mkdir(saves_dir)

urls = [
    'https://ya.ru',
    'https://github.com/RomanKostikov',
    'https://google.com',
    'https://gb.ru',
    'https://mail.ru',
    'https://www.python.org/',
    'https://habr.com/ru/all/',
    'https://learn.microsoft.com/',
    'https://news.vtomske.ru/',
    'https://www.1tv.ru/',
]


def download_content(url: str):
    response = requests.get(url)
    filename = (
            url.replace('https://', '').replace('.', '_').replace('/', '-')
            + '_proc.html'
    )
    with open(os.path.join(saves_dir, filename), 'w', encoding='utf-8') as f:
        f.write(response.text)


processes = []

if __name__ == '__main__':
    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=download_content, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Completed download in {time.time() - start_time} seconds.')

# Вывод в консоль:
# Completed download in 1.5255579948425293 seconds.
