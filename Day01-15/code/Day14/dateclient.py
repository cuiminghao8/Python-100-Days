from socket import socket

def main():
    #1：创建套接字对象默认使用IPV4和TCP
    client= socket()
    #2：连接到服务器（需要指定IP地址和端口）
    client.connect(('10.110.47.27', 6789))
    #3: 从服务器收数据
    
    while True:
        data = client.recv(1024).decode('utf-8')
        if data is not '':
            print(data)
        else:
            return False

    client.close()


if __name__ == '__main__':
    main()


