#!/usr/bin/env python
import logging
import logging.handlers
import socket
import SocketServer
import SimpleHTTPServer
import sys
import os
from time import sleep
from urlparse import urlparse, parse_qs
import signal
import time
print 'Mpu server started'
def signal_handler(signal, frame):
httpd.shutdown
print 'You pressed Ctrl+C!'
sys.exit(0)
PORT = 8000
class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
def log_message(self, format, *args):
return
def do_GET(self):
print self.path
print 'Mpu server request'
if self.path[0:9]=='/logfiles':
print "hello my friend"
self.send_response(200)
self.send_header('Content-type','text/html')
self.end_headers()
self.wfile.write('''
<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="UTF-8">
<title>Page test</title>
</head>
<body>
Resin test
</body>
</html>''')
return
else:
#serve files, and directory listings by following self.path from
#current working directory
SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
signal.signal(signal.SIGINT, signal_handler)
httpd = SocketServer.ThreadingTCPServer(('', PORT),CustomHandler)
print "serving at port", PORT
httpd.serve_forever()
