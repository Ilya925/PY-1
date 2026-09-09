import time
from time import sleep
from threading import Thread

from декораторы import time_run


class WorkThread(Thread):
    def __init__(self, num, tab, vol, dur):
        super().__init__()
        self.num = num
        self.tab = tab
        self.vol = vol
        self.dur = dur


    def run(self):
        print(f'Поток {self.num} started')
        for  k in range(self.vol):
            print(f'{self.tab} Поток {self.num} => Действие № {k + 1}')
            sleep(self.dur)
        print(f'Поток {self.num} stopped')



def f1(n):
    print(n ** 2)
    time.sleep(3)
    print('f1 completed')


def f2(n):
    print(n * 2)
    time.sleep(2)
    print('f2 completed')

@time_run
def main():
    # f1(5)
    # f2(50)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    thread1 = Thread(target=f1, args=(5,))
    thread2 = Thread(target=f1, args=(50,))

    main()