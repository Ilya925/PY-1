from Потоки import WorkThread
from time import sleep


print(f'Основной поток  started')
thread1 = WorkThread(1, '\t\t', 5, 4)
thread2 = WorkThread(2, '\t\t\t\t', 5, 3)
thread3 = WorkThread(3, '\t\t\t\t\t\t', 5, 2)
thread1.start()
thread2.start()
thread3.start()

for k in range(5):
    print(f'Основной Поток => Действие № {k + 1}')
    sleep(1)
print(f'Основной Поток stopped')

thread1.join()
thread2.join()
thread3.join()