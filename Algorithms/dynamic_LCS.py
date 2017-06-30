# -*- coding:utf-8 -*-

""" 
    运用动态规划得出最长公共子序列
"""


def dynamic_lcs(string1, string2):
    length1, length2 = len(string1), len(string2)
    r = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]

    for i in range(length1):
        for j in range(length2):
            if string1[i] == string2[j]:
                r[i + 1][j + 1] = r[i][j] + 1
            else:
                r[i + 1][j + 1] = max(r[i][j + 1], r[i + 1][j])

    return r[length1][length2]


if __name__ == '__main__':
    a = 'ABCBDAB'
    b = 'BDCABA'
    print(dynamic_lcs(a, b))
