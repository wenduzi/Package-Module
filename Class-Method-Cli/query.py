#! /usr/bin/env python
# -*- coding: utf-8 -*-


import cgi


form = cgi.FieldStorage()
print '<html>'
print '<title>Reply Page</title>'
if 'user' not in form:
    print '<h1>Who are you?</h1>'
else:
    print'<h1>Hello <i>%s</i>! </h1>' % cgi.escape(form['user'].value)
print '</html>'
