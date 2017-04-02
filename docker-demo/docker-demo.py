#!/usr/bin/env python3


from http.server import BaseHTTPRequestHandler, HTTPServer
import socket, os, shutil
import sys


PORT=8080

VERBOSE=0
VERBOSE=1
 
HOSTNAME = socket.gethostname()

BASE_IMAGE_PATH  = 'static/img/docker'
BASE_IMAGE_PATH += '_blue'

IMAGE_PATH = BASE_IMAGE_PATH + '.png'


class dockerDemoHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def _createHtmlWelcome(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        file = open('index.html', 'r')
        message = ''.join(file.readlines())
        message = message.replace('{{ Hostname }}', HOSTNAME)
        message = message.replace('Hostname', HOSTNAME)
        if VERBOSE > 0:
            print('Sending back file <{}> as text/html'.format('index.html'))
        return message


    def _createTextWelcome(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/txt')
        self.end_headers()
        IMAGE_PATH = BASE_IMAGE_PATH + '.txt'
        file = open(IMAGE_PATH, 'r')
        message = ''.join(file.readlines())
        yellow_colour = '\x1b[1;33m'
        normal_colour = '\x1b[0;0m'
        message += '\n\n' + yellow_colour + 'Served from ' + HOSTNAME + normal_colour + '\n\n'
        if VERBOSE > 0:
            print('Sending back file <{}> as text/txt'.format(IMAGE_PATH))
        return message

    def send_head(self):
        path = self.path[1:]
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        try:
            # Always read in binary mode.
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f

    def _sendFile(self):
        filepath = self.path[1:]
        f = self.send_head()
        if f:
            shutil.copyfileobj(f, self.wfile)
            f.close()


    def do_GET(self):
        if self.path == '/':
            if 'User-Agent' in self.headers and ('wget' in self.headers['User-Agent'].lower() or 'curl' in self.headers['User-Agent'].lower()):
                message = self._createTextWelcome()
            else:
                message = self._createHtmlWelcome()
            self.wfile.write(bytes(message, 'utf8'))
        else:
            self._sendFile()

    def guess_type(self, path):
        ext = path[path.rfind('.') + 1:].lower()
        print('ext=' + ext)
        if ext == 'htm':
            return 'text/html'
        if ext == 'html':
            return 'text/html'
        if ext == 'css':
            return 'text/css'
        if ext == 'png':
            return 'image/png'
        return 'application/octet-stream'

def httpServer(port):
    print('starting server, listening on port {} ...'.format(port))
           
    # Server settings
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, dockerDemoHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

##----------------------------------------------------------------------
# Args:

a=1
port=PORT

while a < len(sys.argv):

    if sys.argv[a] == '-p':
        a += 1
        port=int(sys.argv[a])
        a += 1
        continue

    print("Error: unknown option: <" + sys.argv[a] + ">")
    sys.exit(1)


##----------------------------------------------------------------------
# Main:

httpServer(port)


