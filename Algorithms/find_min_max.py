# -*- coding:utf-8 -*-

""" 寻找最大值与最小值 """


def find_min(array):
    """ 总共需要比较len(array) - 1 次 """
    _min = array[0]
    for _ in range(1, len(array)):
        if _min > array[_]:
            _min = array[_]
    return _min


def find_max(array):
    """ 总共需要比较len(array) - 1 次 """
    _max = array[0]
    for _ in range(1, len(array)):
        if _max < array[_]:
            _max = array[_]
    return _max


def find_min_and_max(array):
    """ 同时寻找数组中的最小值与最大值 
        总共需要比较 1 + (len(array) - 1 or 2) * 3 / 2
    """

    if len(array) % 2:
        # 数组长度为奇数，取第一个元素为初始最小和最大值
        _min = _max = array[0]
        start = 1
    else:
        # 数组长度为偶数，取前两个元素为初始最小和最大值
        if array[0] > array[1]:
            _min, _max = array[1], array[0]
        else:
            _min, _max = array[0], array[1]
        start = 2
    for _ in range(start, len(array), 2):
        n, m = array[_], array[_ + 1]
        # 成对的处理元素，
        # 先将两个元素自身进行比较，
        # 再将两个元素中较小的与当前最小值进行比较，较大的与当前最大值进行比较
        # 每2个元素只需比较三次。
        if n > m:
            if n > _max:
                _max = n
            if m < _min:
                _min = m
        else:
            if m > _max:
                _max = m
            if n < _min:
                _min = n
    return _min, _max

if __name__ == '__main__':
    a = [35, 40, 88, 88, 77, 12, 8, 10, 25, 46, 39, 70, 1, 99]
    print(find_min_and_max(a))
    # 1, 99
