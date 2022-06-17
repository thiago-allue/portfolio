from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>GET</h1></body></html>".encode())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST</h1></body></html>")


def serve(s):
    s.serve_forever()


address = ('', 8000)
httpd = HTTPServer(address, S)
print('Starting Web Server...')

import time
import threading
t = threading.Thread(target=serve, args=(httpd,), daemon=True)
print('Starting thread')
t.start()

print('Thread started')
while 1:
    time.sleep(0.001)
t.join()
