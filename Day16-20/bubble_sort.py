from time import time
def bubble_sort(origin_items, comp=lambda x , y : x > y):
    """高质量冒泡排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range (i , len(items) - 1 - i):
            if comp(items[j],items[j+1]):
                items[j] , items[j + 1] = items[j + 1] , items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i , i , -1):
                if comp(items[ j - 1], items[j]):
                    items[j] , items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def main():
    start = time()
    list = [1,20,5,2342]
    comp_list = bubble_sort(list)
    end = time()
    print(comp_list)
    print('处理时间：%.5f' %(end - start))

if __name__ == '__main__':
    main()