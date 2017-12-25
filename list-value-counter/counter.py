#! /usr/bin/env python
# -*- coding : utf-8 -*-


# put list value's count into the dict
def counter(lan):
    count = {}
    for i in lan:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print count


if __name__ == '__main__':
    x = ['python', 'java', 'python', 'php', 'php', 'java', 'java', 'php']
    counter(x)
