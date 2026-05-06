import difflib

text1=""" test1 #定义字符串
hellow
my name is machanwei!
difflib document v7.4
add str
"""

text1_ln = text1.splitlines()

text2="""text2:   #定义字符串2
hellow
my name is machangwei!
difflib document v7.5
"""

text2_ln = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_ln,text2_ln)
print('\n'.join(list(diff)))