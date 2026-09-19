import multiprocessing as mp
import time
import random
from math import sqrt


def producer(queue, n_items):
    for i in range(n_items):
        item = sqrt(random.randint(1, 100)) ** 2
        queue.put(item)
        print(f'Производитель сделал {item}')
        time.sleep(random.uniform(0.1, .5))
    queue.put(None)
    print('Производитель работу завершил!')


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        result = sqrt(item ** 2) ** 3
        print(f'Получен {item} => {result}')
        time.sleep(random.uniform(0.2, .6))
    print('Пользователь работу завершил!')


if __name__ == '__main__':
    queue = mp.Queue()
    p_producer = mp.Process(target=producer, args=(queue, 10))
    p_consumer = mp.Process(target=consumer, args=(queue,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()
    print('Главный процесс завершен!')

