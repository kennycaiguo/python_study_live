"""
http built-in module
"""

import sys
from http.server import HTTPServer,SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler

if __name__ == '__main__':
    port = sys.argv[2]
    host = sys.argv[1]
    server_addr = (host,int(port))
    httpd = HTTPServer(server_addr,Handler)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        httpd.server_close()
        sys.exit(0)


