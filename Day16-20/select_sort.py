from time import time

def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = 1
        for j in range(i+1 , len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
            items[i] , items[min_index] = items[min_index], items[i]
        return items

def main():
    start = time()
    list = [1,20,5,2342,61,301,486,184,283,12,593,21,1234,1234,4576,4567,456,245,7,3456,2,1345,34,124,124]
    comp_list = select_sort(list)
    end = time()
    print(comp_list)
    print('处理时间：%.5f' %(end - start))

if __name__ == '__main__':
    main()