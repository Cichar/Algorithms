# -*- coding:utf-8 -*-

""" KMP算法实现 """


# class KMP(object):
#     def __init__(self, target, part):
#         """
#         :param target: 目标字符串
#         :param part  : 模式字符串
#         """
#
#         self._target = target
#         self._part = part
#         self._result = self.kmp_match()
#
#     def __create_next__(self):
#         """ 构建next数组
#             __create_next__('ABCDABD') = [0, 0, 0, 0, 1, 2, 0]
#         """
#         # 生成前缀
#         prefix = {self._part[:i] for i in range(1, len(self._part))}
#         postfix = {}
#         next_list = [0]
#         # 生成next数组
#         for i in range(1, len(self._part)):
#             # 生成每个子串的后缀
#             # 'ABCDABD'
#             # {'B'}
#             # {'BC', 'C'}
#             # {'CD', 'BCD', 'D'}
#             # {'BCDA', 'CDA', 'A', 'DA'}
#             # {'DAB', 'BCDAB', 'AB', 'CDAB', 'B'}
#             # {'BCDABD', 'BD', 'D', 'ABD', 'CDABD', 'DABD'}
#             postfix = {self._part[j:i + 1] for j in range(1, i + 1)}
#             # 计算并向next_list添加每一位的适配度
#             next_list.append(len((prefix & postfix or {''}).pop()))
#         return next_list
#
#     def kmp_match(self):
#         """ kmp算法 """
#
#         target_len = len(self._target)
#         part_len = len(self._part)
#         next_list = self.__create_next__()
#         cur = 0
#         # 即便一位一位右移，最坏的情况有 target_len - part_len 次需要右移
#         while cur <= target_len - part_len:
#             # 匹配子串
#             for i in range(part_len):
#                 if self._target[i + cur] != self._part[i]:
#                     # 出现了不匹配的坏字符，则进行右移
#                     # 移动位数 = 已匹配的字串长度 - 字符匹配度
#                     # 最少像右移动一位
#                     cur += max(i - next_list[i - 1], 1)
#                     break
#             else:
#                 return cur
#         return -1
#
#     def __str__(self):
#         return '%s' % self._result


def kmp_match(target, part):
    """ kmp算法 """

    def create_next():
        """ 构建next数组 
            create_next('ABCDABD') = [0, 0, 0, 0, 1, 2, 0]
        """
        # 生成前缀
        prefix = {part[:i] for i in range(1, len(part))}
        postfix = {}
        _ = [0]
        # 生成next数组
        for i in range(1, len(part)):
            # 生成每个子串的后缀
            # 'ABCDABD'
            # {'B'}
            # {'BC', 'C'}
            # {'CD', 'BCD', 'D'}
            # {'BCDA', 'CDA', 'A', 'DA'}
            # {'DAB', 'BCDAB', 'AB', 'CDAB', 'B'}
            # {'BCDABD', 'BD', 'D', 'ABD', 'CDABD', 'DABD'}
            postfix = {part[j:i + 1] for j in range(1, i + 1)}
            # 计算并向next_list添加每一位的适配度
            _.append(len((prefix & postfix or {''}).pop()))
        return _

    target_len = len(target)
    part_len = len(part)
    next_list = create_next()
    cur = 0
    # 即便一位一位右移，最坏的情况有 target_len - part_len 次需要右移
    while cur <= target_len - part_len:
        # 匹配子串
        for i in range(part_len):
            if target[i + cur] != part[i]:
                # 出现了不匹配的坏字符，则进行右移
                # 移动位数 = 已匹配的字串长度 - 字符匹配度
                # 最少像右移动一位
                cur += max(i - next_list[i - 1], 1)
                break
        else:
            return cur
    return -1

if __name__ == '__main__':
    a = kmp_match('fergdvwertergasfwqerfdsf', 'terg')
    print(a)
