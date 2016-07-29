"""
RUN with python -m SimpleHTTPServer 8000

Serves static files relative to the current running directory
"""

import SimpleHTTPServer
import SocketServer

PORT = 8000

handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), handler)

httpd.serve_forever()
