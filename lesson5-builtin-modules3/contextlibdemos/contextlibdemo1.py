import requests


class Request:
    def __init__(self):
        self.session = requests.session()

    def get(self, url, headers=None):
        if headers is None:
            headers = {}

        response = self.session.get(url)
        return response


class Context:
    def __init__(self):
        print("int __init__")

    def __enter__(self):
        print("int __enter__")
        return Request()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("in __exit__")


if __name__ == '__main__':
    with Context() as t:
        req = t.get("https://wwww.baidu.com")
        print(req.text)

