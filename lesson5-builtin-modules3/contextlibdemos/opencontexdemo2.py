import contextlib

@contextlib.contextmanager
def myopen(filename,mode):
    fp = open(filename,mode)
    try:
        yield fp
    finally:
        fp.close()    


# write file        
# with myopen('test1.txt', 'a') as file_obj:  # with open() as的原理
#     file_obj.write("hello 6666 \n")
#     file_obj.write("world 8888 \n")

# read file
with myopen("test1.txt",'r') as f:
    print(f.read())