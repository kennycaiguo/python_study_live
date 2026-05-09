"""
Python 中的html 模块包含两个函数：escape() 和unescape()。
这里我们来学习HTMLParser类的使用
"""
from html.parser import HTMLParser

class MyHtmlparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
         print("Found a start tag:", tag)
    
    def handle_endtag(self, tag):
        print("Found an end tag :", tag)
    
    def handle_data(self, data):
        print("Found some data  :", data)
    


if __name__ == '__main__':
    myparser = MyHtmlparser()
    myparser.feed('<!DOCTYPE html><html><head><title>Python HTML Module</title></head><body><h2 style="text-align:center;">Hi , I am the HTML code</h2></body></html>')
    


