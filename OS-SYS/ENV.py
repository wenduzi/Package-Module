#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys


# 查看,设置环境变量PYTHONPATH
def env():
    os.environ['PYTHONPATH'] = '/home/'
    os.system('python SysPath.py')     # 被调用的子进程会继承PYTHONPATH到子进程的sys.path中

    reply = sys.stdin.readlines()                                   # 标准输入,也可以用input(),但是不能用sort()了
    reply.sort()
    if reply:
        for num in reply:
            num = int(num)
            print("%d squared is %d" % (num, num ** 2))             # 标准输出
    print('Bye')

if __name__ == '__main__':
    env()

# python ENV.py <input.txt >output.txt                             # 标准输入从文件读取，标准输出到文件
