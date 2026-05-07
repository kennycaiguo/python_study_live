import traceback
# demo 1
# def fun1():
#     fun2(10,0)

# def fun2(a,b):
#     return a/b    

# try:
#     fun1()
# except:
#    traceback.print_exc() # ZeroDivisionError: division by zero

# # demo2
# import traceback

# # declaring array
# A = [1, 2, 3, 4]

# try:
#     value = A[5]
    
# except:
#     # printing stack trace
#     traceback.print_exc()

# # out of try-except
# # this statement is to show that the program continues 
# # normally after the exception is handled
# print("end of program")

# # demo3
# import traceback
# import sys

# a=3
# b=0
# try:
#     a/b
# except Exception as e:
#     exc_type, exc_value, exc_tb = sys.exc_info()
#     tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
#     print(''.join(tb.format_exception_only())) # ZeroDivisionError: division by zero

# # # demo4
# # importing the modules
# import traceback
# import sys

# def call1(f):

#   # inside call1()
#   # call1() calling call2()
#   call2(f)

# def call2(f):
#   # inside call2()
#   # calling f()
#   f()

# def f():
  
#     # inside f()
#     summary = traceback.StackSummary.extract(
#         traceback.walk_stack(None)
#     )
#     print(''.join(summary.format()))

# # calling f() using call1()
# call1(f)

# demo
import traceback
import sys

def call1(f):

    # inside call1()
    # call1() calling call2()
    call2(f)

def call2(f):
    # inside call2()
    # calling f()
    f()
    
template = (
    '{frame.filename}:{frame.lineno}:{frame.name}:\n'
    '    {frame.line}'
)

def f():
    summary = traceback.StackSummary.extract(
        traceback.walk_stack(None)
    )
    for frame in summary:
        print(template.format(frame=frame))

# calling f() through call1()
call1(f)