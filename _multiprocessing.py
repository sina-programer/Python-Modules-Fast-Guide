import multiprocessing
import time

def timer(name, times):
    for i in range(1, times+1):
        print(name, i, sep=': ')
        time.sleep(1)


if __name__ == "__main__":
    timer1 = multiprocessing.Process(target=timer, args=('First-10', 10))
    timer2 = multiprocessing.Process(target=timer, args=('Second-8', 8))
    timer1.start()
    timer2.start()
