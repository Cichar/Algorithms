# -*- coding:utf-8 -*-

"""
    坏字符规则：
        后移位数 = 坏字符的位置 - 搜索词中的上一次出现位置
        例如：
            字符串: "HERE IS A SIMPLE EXAMPLE"
            搜索串: "EXAMPLE"
            以S为例，它对应搜索串第6位， 上一次出现在搜索词的''-1''(未出现)
            即：
                后移 = 6 - (-1) = 7
                "HERE IS A SIMPLE EXAMPLE"
                       "EXAMPLE"
            再以P为例，对应搜索串的第6位，在搜索词的上一次第4位
            即：
                后移 = 6 - 4 = 2
                "HERE IS A SIMPLE EXAMPLE"
                         "EXAMPLE"
                         
    好后缀规则：
        (1) "好后缀"的位置以最后一个字符为准。假定"ABCDEF"的"EF"是好后缀，则它的位置以"F"为准，即5（从0开始计算）。
        (2) 如果"好后缀"在搜索词中只出现一次，则它的上一次出现位置为 -1。比如，"EF"在"ABCDEF"之中只出现一次，
            则它的上一次出现位置为-1（即未出现）
        (3) 如果"好后缀"有多个，则除了最长的那个"好后缀"，其他"好后缀"的上一次出现位置必须在头部。
            比如，假定"BABCDAB"的"好后缀"是"DAB"、"AB"、"B"，请问这时"好后缀"的上一次出现位置是什么？
            回答是，此时采用的好后缀是"B"，它的上一次出现位置是头部，即第0位。
            这个规则也可以这样表达：如果最长的那个"好后缀"只出现一次，
            则可以把搜索词改写成如下形式进行位置计算"(DA)BABCDAB"，即虚拟加入最前面的"DA"。
            
        后移位数 = 好后缀的位置 - 搜索词中的上一次出现位置
        
        例如：
            "HERE IS A SIMPLE EXAMPLE"
                     "EXAMPLE"
            所有的"好后缀"（MPLE、PLE、LE、E）之中，只有"E"在"EXAMPLE"中并且还出现在头部，
            所以：
                后移 = 6(E在搜索词中的位置) - 0(E在搜索词中的上一次的位置) = 6。
                "HERE IS A SIMPLE EXAMPLE"
                               "EXAMPLE"
    
    ""基本思想"" : 每次后移这两个规则之中的较大值。
    
"""


def bm_match(target, part):
    target_len = len(target)
    part_len = len(part)
    # 临时长度
    _ = len(part)
    cur = 1

    def bad():
        """ 生成坏词规则 
            构建搜索词中各字符上一次出现位置
        """
        _dict = {}
        for index, value in enumerate(part):
            _dict[value] = index
        return _dict

    def good_postfix(cur):
        """ 生成好后缀规则 
            做好后缀和前缀的匹配
            # >>> b = 'EXAMPLE'
            # >>> for i in range(4,0,-1):
            # ...     print(b[-i:],b[:i], i)
            # ...
            # MPLE EXAM 4
            # PLE EXA 3
            # LE EX 2
            # E E 1
        """
        for i in range(cur, 0, -1):
            if part[-i:] == part[:i]:
                return i - 1
        return 0

    bad_dict = bad()
    while part_len <= target_len:
        # 判断part与target对应位是否相同
        if part[-cur] == target[_ - cur]:
            cur += 1
            if cur > part_len:
                return _ - part_len
        else:
            b = (part_len - cur) - bad_dict.get(target[_ - cur], -1)
            g = 0
            # 好后缀大于1个才进行好后缀匹配
            if cur > 1:
                g = part_len - good_postfix(cur)
            _ += max(b, g)
            cur = 1
    return -1


if __name__ == '__main__':
    print(bm_match('HERE IS A SIMPLE EXAMPLE', 'EXAMPLE'))
