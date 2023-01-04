import os
import http.server
import socketserver
import pathlib

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            file_path = pathlib.Path('home.html')
            if file_path.is_file():
                self.send_response(HTTPStatus.OK)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                with file_path.open('rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(HTTPStatus.NOT_FOUND)
                self.end_headers()
        else:
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            msg = 'Hello! you requested %s' % (self.path)
            self.wfile.write(msg.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
