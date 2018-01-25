#! /usr/bin/env python
# -*- coding:utf-8 -*-

from operator import itemgetter
import sys

current_time = None
current_count = 0
time = None

for line in sys.stdin:
    line = line.strip()
    time, count = line.split('\t', 1)
    count = int(count)

    if current_time == time:
        current_count += count
    else:
        if current_time:
            print(current_time, current_count)
        current_time = time
        current_count = count
