"""
Python 中的html 模块包含两个函数：escape() 和unescape()。
"""
import html

def escapedemo():
    html_code = '<!DOCTYPE html> <html> <head> <title>Python HTML Module</title></head><body><h2 style="text-align:center;">Hi , I am the HTML code</h2></body></html>'

    encoded_code = html.escape(html_code)
    print(encoded_code)

def escapedemo2():
    html_code = '<!DOCTYPE html> <html> <head> <title>Python HTML Module</title></head><body><h2 style="text-align:center;">Hi , I am the HTML code</h2></body></html>'

    encoded_code = html.escape(html_code,quote=False)
    print(encoded_code)

def unescapedemo():
    encoded_code = '&lt;&amp;!DOCTYPE html&gt; &lt;html&gt; &lt;head&gt; &lt;title&gt;Python HTML Module&lt;/title&gt;&lt;/head&gt;&lt;body&gt;&lt;h2 style=&quot;text-align:center;&quot;&gt;Hi , I am the HTML code&lt;/h2&gt;&lt;/body&gt;&lt;/html&gt;'

    html_code = html.unescape(encoded_code)
    print(html_code)

if __name__ == '__main__':
    # escapedemo()
    # escapedemo2()
    unescapedemo()
