import time
import requests
from multiprocessing.pool import ThreadPool


def get_html_info(url):
    response = requests.get(url)
    return response


urls = ['https://www.google.com', 'https://www.python.org',
        'https://www.rambler.ru', 'https://www.mail.ru',
        'https://www.github.com']
start_time = time.time()
with ThreadPool(len(urls)) as executor:
    response = executor.map(get_html_info, urls)
for element in response:
    print(f'Количество символов на странице {element.url} составляет {len(element.text)}')
parallel_working_time = time.time() - start_time
start_time = time.time()
for url in urls:
    response = get_html_info(url)
    print(f'Количество символов на странице {response.url} составляет '
          f'{len(response.text)}')
sequential_working_time = time.time() - start_time
print(f'Время параллельной работы составило: {parallel_working_time},\n'
      f'Время последовательной работы составило: {sequential_working_time}\n'
      f'Время последовательной работы в {sequential_working_time / 
      parallel_working_time} раз дольше.')