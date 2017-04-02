#!/usr/bin/env python3

# Inpsired by:
#    https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3
#
# and SimpleHTTPServer

from http.server import BaseHTTPRequestHandler, HTTPServer
import socket, os
import shutil

HOSTNAME = socket.gethostname()

VERBOSE=0
VERBOSE=1

# To be supplemented with colour and filetype:
BASE_IMAGE_PATH='static/img/docker_'
BASE_IMAGE_PATH+='blue'

# Default: return html page with png image
IMAGE_PATH=BASE_IMAGE_PATH+'.png'

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def _createTextWelcome(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/txt')
        self.end_headers()

        IMAGE_PATH=BASE_IMAGE_PATH+'.txt'

        file = open (IMAGE_PATH, "r")
        message = ''.join(file.readlines())

        yellow_colour = "\033[1;33m"
        normal_colour = "\033[0;0m"

        message += "\n\n" + yellow_colour + "Served from " + HOSTNAME + normal_colour + "\n\n"

        if VERBOSE > 0:
            print("Sending back file <{}> as text/txt".format(IMAGE_PATH))

        return message

    def _createHtmlWelcome(self):
        # Send response status code
        self.send_response(200)

        self.send_header('Content-type','text/html')
        self.end_headers()

        file = open ('index.html', "r")
        message = ''.join(file.readlines())
        message = message.replace('{{ Hostname }}', HOSTNAME)
        message = message.replace('Hostname', HOSTNAME) # in case

        if VERBOSE > 0:
            print("Sending back file <{}> as text/html".format('index.html'))

        return message

    ## From SimpleHTTPServer:
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
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found (" + path + ")")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()

        if VERBOSE > 0:
            print("Sending back file <{}> as type <{}>".format(path, ctype))

        return f

    def guess_type(self, path):
        """Simplified version just detecting our few file types"""

        # very basic, limited mimetype handling:
        ext=path[ path.rfind(".")+1 : ].lower()
        print("ext=" + ext)

        if ext == "htm":
            return 'text/html'
        if ext == "html":
            return 'text/html'

        if ext == "css":
            return 'text/css'

        if ext == "png":
            return 'image/png'

        return 'application/octet-stream' # Default

    def _sendFile(self):
        filepath = self.path[1:]

        f = self.send_head()
        if f:
            shutil.copyfileobj(f, self.wfile)
            f.close()


    # GET
    def do_GET(self):
              
        ############################################
        # Detect if we have a text-mode browser
        # If text-mode return ascii-art
        # print("dir(req):"); print(str( dir( self ) ))
        # print("dir(req.headers):"); print(str( self.headers ))

        if self.path == '/':
            if "User-Agent" in self.headers and \
                ( "wget" in self.headers["User-Agent"].lower() or \
                  "curl" in self.headers["User-Agent"].lower() ):
                message = self._createTextWelcome()
            else:
                message = self._createHtmlWelcome()

            # Send message back to client
            # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))

        else:
            self._sendFile()

        return
 
def run():
    print('starting server...')
 
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()
 
run()

