# -*- coding:utf-8 -*-

""" **insertion_sort** 
    时间花费：c1 * n * n
    c1是一个不依赖于n的常数
"""


def insertion_sort(arr, reverse=False):
    if not reverse:
        for j in range(len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key
    else:
        for j in range(len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] < key:
                arr[i + 1] = arr[i]
                i -= 1
            arr[i + 1] = key
    return arr

if __name__ == '__main__':
    print(insertion_sort([5, 2, 4, 6, 1, 3]))
    print(insertion_sort([5, 2, 4, 6, 1, 3], reverse=True))
