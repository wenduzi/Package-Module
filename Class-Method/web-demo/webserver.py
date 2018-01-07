#! /usr/bin/env python3.5

import os
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 8080

os.chdir(webdir)
srvaddr = ("", port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()
