"""
interact closely with the Python interpreter and its runtime environment
properties
sys.version
sys.argv
sys.modules  # show python built-in modules
sys.path # interpreter search path
sys.stdin
sys.stdout 
mothods:
sys.exit() # quit the program
"""
import sys

print(sys.version) # property,not function 3.11.9
print(sys.argv) # ['d:/pc_programming_live/python_study_live/lesson3-builtin-modules/lesson3-demo3-sys.py']
# print(sys.modules) # show python built-in modules
# print(sys.path) # interpreter search path
# print(sys.platform) # win32
# print(sys.stdin)

# for i in sys.stdin:
#     print(i)
# content = sys.stdin
# print(content)
# sys.stdout.write("hello python") # print()