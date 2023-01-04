import os
import http.server
import socketserver

from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # get the page
        path = self.path
        if path == '/':
            with open('home.html', 'rb') as page:
                self.wfile.write(page.read())
        elif path == '/about':
            with open('about.html', 'rb') as page:
                self.wfile.write(page.read())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
