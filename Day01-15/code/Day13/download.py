from random import randint
from time import time , sleep
from multiprocessing import Process
from os import getpid


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下载完成！ 耗费了%d秒'% ( filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f 秒' % (end - start))

if __name__ == '__main__':
    main()