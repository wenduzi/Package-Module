#! /usr/bin/env python
# -*- coding:utf-8 -*-


# 把行中的'you' 改变为 ‘I'm’
def replacer(line):
    try:
        line = line.replace('you', 'I'+'\''+'m')
        return line
    except KeyError:
        pass
