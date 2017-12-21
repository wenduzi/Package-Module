#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket


# scan ports of host
def scan(ip, ports=None):
    if ports is None:
        ports = range(1, 100)
    for port in ports:
        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            print('%s opened %s' % (ip, port))
        except BaseException as e:
            print('%s closed %s' % (ip, port))
        finally:
            if s:
                s.close()

if __name__ == '__main__':
    scan('localhost', [80, 8080, 22])
