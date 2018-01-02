#! /usr/bin/env python
# -*- coding:utf-8 -*-

wen = {'name': 'wenduzi', 'age': 18, 'pay': 50000, 'job': 'dev'}
li = {'name': 'lilei', 'age': 16, 'pay': 30000, 'job': 'hdw'}
han = {'name': 'hanmeimei', 'age': 15, 'pay': 20000, 'job': None}

db = {}
db['wen'] = wen
db['li'] = li
db['han'] = han

if __name__ == '__main__':
    for key in db:
        print key, '==>\n', db[key] 

