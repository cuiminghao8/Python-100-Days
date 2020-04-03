from time import time
from threading import Thread
import requests

class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('D:\\Download' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    #通过requests模块的get函数获取网络资源
    #下面代码中使用了天行数据接口提供的网络API
    #要使用该数据接口需要再天行数据的网站上注册
    #然后用自己的Key替换掉下面代码中的APIKey即可
    resp = requests.get('http://api.tianapi.com/meinv/?key=6179a5be1756aa09b9842071d26797d8&num=10')
    data_model = resp.json()
    
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        #通过多线程的方式实现图片下载
        DownloadHandler(url).start()
if __name__ == '__main__':
    main()