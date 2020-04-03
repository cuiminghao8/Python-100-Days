def main():
    try:
        f = open('C:\\Users\\minghao.cui\\Desktop\\Python-100-Days\\Day01-15\\code\\Day11\\致橡树.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()