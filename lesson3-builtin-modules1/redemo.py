"""
re built-in module
methods:
re.match(pattern,string,flags=0) # success->return matched object,None otherwise
re.compile(pattern)  # return a regexp object
re.search() # search for first success match,or None if no result
re.findall() # return a list of all matched sub string ,or None if no match found
re.finditer() # return a iteritor of all matched sub string ,or None if no match found
re.sub(pattern,repl,string,count=0,flags=0) # replace the mathed
re.subn(pattern,repl,string,count=0,flags=0) # replace the mathed and return a tuple of (str,times replaced)
re.split(pattern,string,maxsplit=0,flags=0) # use the match to cut the string,return a list
"""
import re

# 1.match(pattern,string,flags=0)，只会返回第一个匹配结果
"""
从字符串的开头进行匹配， 匹配成功就返回一个匹配对象，匹配失败就返回None
若匹配到，通过调用group()方法得到匹配的字符串并返回
"""
# print("匹配到的字符串为:",re.match("ac","acd").group()) # 输出 ：匹配到的字符串为: ac
# print("匹配到的字符串为:",re.match("hello","hello world,hello guys,hello girls").group()) # 输出 ：匹配到的字符串为: hello

# 2.search(pattern,string,flags=0) ,只会返回第一个匹配结果
"""
搜索整个字符串去匹配第一个并返回，未匹配成功返回None
若匹配到，通过调用group()方法得到匹配的字符串并返回
"""
# print("匹配到的字符串为:",re.search("ac","ddacd").group())# 输出 ：匹配到的字符串为: ac
# print("匹配到的字符串为:",re.search("hello","hello world,hello guys,hello girls").group()) # 输出 ：匹配到的字符串为: hello

 # 3. findall(pattern, string, flags=0)
"""
match和search均用于匹配单值，即：只能匹配字符串中的一个，如果想要匹配到字符串中所有符合条件的元素，则需要使用 findall。
"""

# print("匹配到的字符串为:",re.findall("ac","dacdacd")) ##输出：匹配到的字符串为: ['ac', 'ac']
# print("匹配到的字符串为:",re.findall("hello","hello world,hello guys,hello girls")) # ['hello', 'hello', 'hello']

# 4. sub(pattern,repl,string,count=0,flags=0)
"""
替换匹配成功的指定位置字符串
"""
# res = re.sub('\d','py','doc.2.exe.3.xls')
# print("替换数字为py:",res) #输出 ：替换数字为py: doc.py.exe.py.xls
# res = re.sub('hello','hey','hello world,hello guys,hello girls') 
# print("替换结果为py:",res) #输出 ：hey world,hey guys,hey girls

# 5.split(pattern,string,maxsplit=0,flags=0)
"""
根据正则匹配分割字符串
"""
# res1=re.split('a','a1bcd')
# print("分割字符得到:",res1)#输出 ：['', '1bcd']

# res1=re.split('and','family and friend and lover and workmate')
# print("分割字符得到:",res1) # 分割字符得到: ['family ', ' friend ', ' lover ', ' workmate']

# 6.compile()
"""
python代码最终会被编译为字节码，之后才被解释器执行。
在模式匹配之前，正在表达式模式必须先被编译成regex对象，
预先编译可以提高性能，re.compile()就是用于提供此功能
"""
# obj=re.compile('\d{3}')
# ret=obj.search('abcd123edee')
# print(ret) # <re.Match object; span=(4, 7), match='123'>
# print(ret.group())#输出 ：123

# obj=re.compile('\d{2}')
# ret=obj.search('abcd123edee22hello6world11of8python123')
# print(ret.group())  # 12
# print(obj.findall('abcd123edee22hello6world11of8python123')) # ['12', '22', '11', '12']


