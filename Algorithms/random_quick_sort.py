# -*- coding:utf-8 -*-

import random

""" 快速排序 - 随机版
    时间花费：n^2
"""


def partition(array, start, end):
    """ 过程模拟：
        array = [5, 8, 2, 4]
        partition(array, 0, 3)
        # >>> x = 4
        # >>> i = -1
        # >>> for j in range(0, 3):
        # >>> j = 2
        # >>> array[2] <= x
        # >>> 2 <= 4
        # >>> i = 0
        # >>> array[0], array[2] = array[2], array[0]
        # >>> array[0], array[2] = 2, 5
        # >>> array = [2, 8, 5, 4]
        # >>> array[1], array[3] = 4, 8
        # >>> array = [2, 4, 5, 8]
        不断的将比最后一个元素小的元素与前面大的元素进行交换，
        第一个区域均是比最后一个元素小的元素，
        第二个区域均是比最后一个元素大的元素，
        最后将最后一个元素与第二个区域的第一个元素进行交换，
        则得到了''中间元素''，
        满足第一区域元素均小于''中间元素''，
        满足第二区域元素均大于''中间元素''，
        最后返回下标
    """
    x = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def random_partition(array, start, end):
    i = random.choice(range(start, end + 1))
    array[end], array[i] = array[i], array[end]
    return partition(array, start, end)


def quick_sort(array, start, end):
    if start < end:
        mid = random_partition(array, start, end)
        quick_sort(array, start, mid - 1)
        quick_sort(array, mid + 1, end)


if __name__ == '__main__':
    a = [5, 8, 2, 4, 1, 9, 7, 6, 3]
    quick_sort(a, 0, 8)
    print(a)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
