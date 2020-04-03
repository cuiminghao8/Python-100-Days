import json

def main():
    dir = 'C:\\Users\\minghao.cui\\Desktop\\Python-100-Days\\Day01-15\\code\\Day11\\'
    mydict = {
        'name' : '崔明浩',
        'age' : '31',
        'qq' : 695396707,
        'friends' : ['王大锤' , '百元芳'],
        'cars' : [
            {'brand' : 'BYD' , 'max_speed' : 180},
            {'brand' : 'Audi' , 'max_speed' : 280},
            {'brand' : 'Benz' ,  'max_speed' : 320}
        ]
    }
    try:
        with open(dir + 'data.json' , 'w' , encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

if __name__ == '__main__':
    main()