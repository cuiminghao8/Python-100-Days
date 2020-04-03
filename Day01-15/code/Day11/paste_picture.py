def main():
    dir = 'C:\\Users\\minghao.cui\\Desktop\\Python-100-Days\\Day01-15\\code\\Day11\\'
    try:
        with open( dir + 'mm.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open( dir + '吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出错')
    print('执行程序结束')

if __name__ == '__main__':
    main()