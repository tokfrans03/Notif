#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import requests
import urllib
from creds import *

port = 8000

def sendnotif(title, message, image=""):
    
    if image == "":
        url = "https://api.pushmealert.com?user="+user+"&key="+key+"&title="+title+"&message="+message
    else:
        url = "https://api.pushmealert.com?user="+user+"&key="+key+"&title="+title+"&message="+message+"&image=" + image

    requests.get(url)

class S(BaseHTTPRequestHandler):
    def send_res(self, args, code=200, Success=True):
        
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        out = {
            "Success": Success,
            "value": args
        }
        self.wfile.write(json.dumps(out).encode('utf-8'))

    def do_OPTIONS(self):
        print("\nPath:", str(self.path),
              "\nHeaders:\n" + str(self.headers))
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_GET(self):

        print("\nPath:", self.path)
        print(self.headers)

        if self.path == "/":

            self.send_res("Do a post with 'title' and 'message' and optionally 'imgurl'")
            return


        self.send_res("No such method, try /", code=404)

        # if self.path == "/mqtt":
        #     self._set_response(data)
        # else:
        #     self._set_response()

        # print("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        # self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        # <--- Gets the size of data
        content_length = int(self.headers['Content-Length'])
        # <--- Gets the data itself
        post_data = self.rfile.read(content_length)
        # print(json.loads(post_data.decode('utf-8')))
        print("\nPath:", str(self.path),
              "\nHeaders:\n" + str(self.headers))
        print(content_length)
        if content_length > 0:
            body = post_data.decode('utf-8')
            print("Body:\n" + body, "\n")
            try:
                body = json.loads(body)
                if "imgurl" in body:
                    sendnotif(body["title"], body["message"], image=body["imgurl"])
                else:
                    sendnotif(body["title"], body["message"])
                self.send_res("Done")
                return

            except:
                self.send_res("Not correct json format", code=500, Success=False)
                return

        else:
            self.send_res(
                "POST request for {} . Please send a body".format(self.path), Success=False)


def run(server_class=HTTPServer, handler_class=S, port=port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port', port, '...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('\nStopping httpd...')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
