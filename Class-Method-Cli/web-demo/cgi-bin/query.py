#! /usr/bin/env python3

import cgi, html, sys, shelve
fieldnames = ['name', 'age', 'job', 'pay']

# form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.append('../..')
from person import Person

form = {'key': 'wen'}


def fetchrecord(db, form):
    try:
        key = form['key']
        record = db[key]
        # object to dict
        fields = record.__dict__
        fields['key'] = key
        return fields
    except:
        # create new dict
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def updaterecord(db, form):
    if 'key' not in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    else:
        key = form['key']
        if key in db:
            record = db[key]
        else:
            record = Person(name='?', age='?')
            for field in fieldnames:
                setattr(record, field, eval(form[field]))
            db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open('../../person-shelve')
print(updaterecord(db, form))


# return "hello 'key'"
# import cgi, html
#
#
# form = cgi.FieldStorage()
# print('Content-type: text/html\n')
# print('<title>Reply Page</title>')
# if 'user' not in form:
#     print('<h1>Who are you?</h1>')
# else:
#     print('<h1>Hello <i>%s</i>! </h1>' % html.escape(form['user'].value))
