""" 
python textwrap builtin module
"""

import textwrap
# textwrap.fill(text, width, **kwargs) 将文本text按width指定的宽度进行包装，并返回包装后的多行字符串。
text = "Python的textwrap库是一个非常有用的文本处理工具，它可以帮助我们轻松地对长文本进行包装。"
# text_wr = textwrap.fill(text,20)
# print(text_wr)
# """
# Python的textwrap库是一个非
# 常有用的文本处理工具，它可以帮助我们轻松
# 地对长文本进行包装。
# """

# # textwrap.wrap(text, width, **kwargs)与fill()类似，但返回的是一个字符串列表，每个元素代表一行。
# text_wr_lst = textwrap.wrap(text,20)
# print(text_wr_lst) # ['Python的textwrap库是一个非', '常有用的文本处理工具，它可以帮助我们轻松', '地对长文本进行包装。']

# # textwrap.indent(text, prefix) 为文本text的每一行添加前缀prefix。
# text_ind = textwrap.indent(textwrap.fill(text,20),"   ")
# print(text_ind)

# # textwrap.dedent(text) 去除文本text中所有行的共同缩进。
# txt = '   你好我好大家好。'
# de_txt = textwrap.dedent(txt)
# print(de_txt)

# # initial_indent和subsequent_indent 这两个参数可以分别设置首行和后续行的缩进。
# text = "Python的textwrap库是一个非常有用的文本处理工具，它可以帮助我们轻松地对长文本进行包装。"
# custom_wrapped_text = textwrap.fill(text, 20, initial_indent='* ', subsequent_indent='  * ')
# print(custom_wrapped_text)

# """
# 处理空白字符
# textwrap库提供了一些参数来控制空白字符的处理，如expand_tabs、replace_whitespace和fix_sentence_endings。

# expand_tabs：将制表符（\t）转换为空格。
# replace_whitespace：将所有连续的空白字符替换为单个空格。
# fix_sentence_endings：尝试修复句子末尾的空格，以便更好地进行包装
# """
# import textwrap
# text = "" \
#        "Python的textwrap库是一个非常有用的文本处理工具，   它可以帮助我们轻松地对长文本进行包装。    "
# fixed_text = textwrap.fill(text, 20, expand_tabs=True, replace_whitespace=True, fix_sentence_endings=True)
# print(fixed_text)

