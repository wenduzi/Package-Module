#! /usr/bin/env python
# -*- coding: utf-8 -*-



def more(text, numlines=2):
    lines = text.splitlines()
    while lines:
        prelines = lines[:numlines]
        lines = lines[numlines:]
        for line in prelines: print(line)
        if lines and str(input('More?')) not in ['Y', 'y']:
            break


if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(), 2)




