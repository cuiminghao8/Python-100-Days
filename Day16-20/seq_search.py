def seq_search(item, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item ==key:
            return index
    return -1

def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


prices = {
    'APPL' : 191.88,
    'GOOG' : 1186.96,
    'IBM' : 149.24,
    'ORCL' : 48.44,
    'ACN' : 166.89,
    'FB' : 208.09,
    'SYNC' : 21.29
}
#用股票价格大于100元的股票构造一个新的字典
prices2 = {key : value for key , value in prices.items() if value > 100}
print(prices2)

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
#录入五个学生三门课程的成绩
scores = [[None] * len(courses) for _ in range(len(names))]
print(scores)
for row , name in enumerate(names):
    for col , course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)

    
