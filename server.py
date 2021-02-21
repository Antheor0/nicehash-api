#!/bin/python3
import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

#port
srvPort=12323

# Make sure the server is created at current directory
os.chdir("/app/data")
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 12323), RequestHandlerClass=CGIHTTPRequestHandler)
#
buffer = 1
sys.stderr = open('logfile.txt', 'w', buffer)

server_object.serve_forever()