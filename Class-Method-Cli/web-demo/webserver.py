#! /usr/bin/env python3

import sys, os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

os.chdir(webdir)
srvaddr = ("", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()