#! /usr/bin/env python
# -*- coding:utf-8 -*-
from replace import replacer


# 导入replacer函数对input进行改变后存储到input.out
def fileoperation(file, function):
    with open(file, 'r') as input123, open(file + '.out', 'w') as output123:
        for line in input123:
            output123.write(function(line))

if __name__ == '__main__':
    fileoperation('input', replacer)
    for line in open('input' + '.out', 'r'):
        print(line)
