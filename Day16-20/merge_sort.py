def merge_sort(items, comp=lambda x,y : x<=y):
    """归并排序（分洽法）"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid],comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)

def merge(items1, items2, comp):
    """合并两个有序的列表合并成一个有序的列表"""
    