#! /usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
from person import Person
from person import Manager


wen = Manager('wenduzi', 18, 50000)
han = Person('hanmeimei', 15, 10000, None)
li = Person('lilei', 16, 30000, 'dev')

db = shelve.open('person-shelve')
db['wen'] = wen
db['han'] = han
db['li'] = li
db.close()

