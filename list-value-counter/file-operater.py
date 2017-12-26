#! /usr/bin/env python
# -*- coding:utf-8 -*-


res = {}

with open('file') as f:
    for char in f.read().replace(' ', ''):
        res[char] = res.get(char, 0)+1
        # if char in res:
        #     res[char] += 1
        # else:
        #     res[char] = 1
print res.items()
for c, num in sorted(res.items(), key=lambda x: x[1], reverse=True)[:3]:
    print '%s is %s' % (c, num)
