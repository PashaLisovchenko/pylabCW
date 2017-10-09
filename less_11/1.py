from celery import Celery
from threading import Lock, Thread, Semaphore
from multiprocessing import Process, Queue, Value, Array
import time

# l = Semaphore()
l = Lock()


def f1(count_file):
    for i in range(int(count_file)):
        with open(str(i)+'.txt', 'w') as f:
            f.write("1")


if __name__=="__main__":
    count_file = input("Enter count file: ")
    count_w_file = input("Enter count w_file: ")
    for i in range(int(count_w_file)):
        Thread(target=f1(count_file)).start()