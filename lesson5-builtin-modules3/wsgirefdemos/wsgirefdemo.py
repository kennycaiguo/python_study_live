from wsgiref.simple_server import make_server
from wsgi_app import simple_app


def wsgiref_demo1():
    with make_server('', 8000, simple_app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()

if __name__ == '__main__':
    wsgiref_demo1()        