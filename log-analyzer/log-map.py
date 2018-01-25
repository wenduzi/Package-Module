#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys


for line in sys.stdin:
    i = 0
    for flow in line.split():
        if i == 1:
            timerow = flow.split(":")
            hm = timerow[0]
            print ('%s\t%s' % (hm, 1))
        i += 1
