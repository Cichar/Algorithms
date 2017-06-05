# -*- coding:utf-8 -*-

""" **merge_sort** 
    时间花费：c2 * n * lgn
    c2是一个不依赖于n的常数
"""


def merge(array, start, mid, end):
    """ 归并排序子程序
    """

    # 数组切片
    len_left = mid - start + 1
    len_right = end - mid

    # 新建缓存数组
    left_arr = []
    right_arr = []
    for _ in range(len_left):
        left_arr.append(array[start + _])
    for _ in range(len_right):
        right_arr.append(array[mid + _ + 1])

    # 设置哨兵
    flag = 1 << 24
    left_arr.append(flag)
    right_arr.append(flag)

    i = j = 0
    # 将原数组中的元素分别进行大小排序替换
    for _ in range(start, end + 1):
        if left_arr[i] <= right_arr[j]:
            array[_] = left_arr[i]
            i += 1
        else:
            array[_] = right_arr[j]
            j += 1


def merge_repeat(array, start, end):
    """ 将数组不断的进行拆分 
        最终将数组化为单个元素，再逐渐进行相邻数组的合并排序
        
        过程模拟：
            [5, 2, 4, 7, 1, 3, 2, 6]        
           [5, 2, 4, 7]  [1, 3, 2, 6]
          [5, 2] [4, 7]  [1, 3] [2, 6]
        [5] [2] [4] [7]  [1] [3] [2] [6]
          [2, 5] [4, 7]  [1, 3] [2, 6]
           [2, 4, 5, 7]  [1, 2, 3, 6]
            [1, 2, 2, 3, 4, 5, 6, 7]
            
    """
    if start < end:
        mid = (end + start)//2
        merge_repeat(array, start, mid)
        merge_repeat(array, mid + 1, end)
        merge(array, start, mid, end)


def merge_sort(array):
    start = 0
    end = len(array) - 1
    merge_repeat(array, start, end)

if __name__ == '__main__':
    arr = [5, 2, 4, 7, 1, 3, 2, 6, 9, 8, 10, 19, 13, 14, 11, 9]
    merge_sort(arr)
    print(arr)
