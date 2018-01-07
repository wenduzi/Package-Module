#! /usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from person import Person


fieldnames = ['name', 'age', 'job', 'pay']
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('person-shelve')

while True:
    key = input('please enter name: ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        newtext = input('%s = %s \n ''  new value?  ' % (field.ljust(maxfield), getattr(record, field)))
        if newtext:
            setattr(record, field, newtext)
    db[key] = record
db.close()
