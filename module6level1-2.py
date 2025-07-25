import time
import threading
from threading import current_thread


def thread_starting_time(thread_name):
    time.sleep(1)
    threading.current_thread().return_value = thread_name


names_pool = ['мыслей', 'сознания', 'воображения', 'рассуждений', 'словесный']
start_time = time.time()
threads = [threading.Thread(target=thread_starting_time, name=name,
                            args=(name, )) for name in names_pool]
for t in threads:
    print(f'Поток {t.name} готовится к старту!')
    t.start()
for t in threads:
    t.join()
    print(f'Поток {t.return_value} запущен!')
parallel_working_time = time.time() - start_time
start_time = time.time()
for name in names_pool:
    print(f'Поток {name} готовится в старту!')
    thread_starting_time(name)
    print(f'Поток {current_thread().return_value} запущен!')
sequential_working_time = time.time() - start_time
print(f'Время параллельной работы составило: {parallel_working_time},\n'
      f'Время последовательной работы составило: {sequential_working_time}\n'
      f'Время последовательной работы в {sequential_working_time / 
      parallel_working_time} раз дольше.')

