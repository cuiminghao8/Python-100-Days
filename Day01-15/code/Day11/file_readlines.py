
import time

def main():
    # 一次性读取整个文件内容
    with open('C:\\Users\\minghao.cui\\Desktop\\Python-100-Days\\Day01-15\\code\\Day11\\致橡树.txt' , 'r' , encoding='utf-8') as f:
        print(f.read())

    #通过for-in循环逐行读取
    with open('C:\\Users\\minghao.cui\\Desktop\\Python-100-Days\\Day01-15\\code\\Day11\\致橡树.txt' , mode='r' , encoding='utf-8') as f:
        for line in f:
            print(line, end=' ')
            time.sleep(0.5)
    print()

    #读取文件按行读取到列表中
    with open ('C:\\Users\\minghao.cui\\Desktop\\Python-100-Days\\Day01-15\\code\\Day11\\致橡树.txt' , mode='r' , encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()