#! /usr/bin/env python
# -*- coding:utf-8 -*-


res = {}

with open('file') as f:
    # f.read()按字符读取，不是按行。
    for char in f.read().replace(' ', ''):
        # get为如果没有此key则设置为0，一行语句可以取代下面的四行语句
        res[char] = res.get(char, 0)+1
        # if char in res:
        #     res[char] += 1
        # else:
        #     res[char] = 1

# res.items() 字典转化为元组，sorted 对元组按key进行排序，lambda是函数f(x)=x[1]的简单表述。
for c, num in sorted(res.items(), key=lambda x: x[1], reverse=True)[:3]:
    print '%s is %s' % (c, num)
