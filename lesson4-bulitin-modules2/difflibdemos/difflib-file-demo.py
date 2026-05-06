import difflib
import sys

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except Exception as e:
    print("Error:"+str(e))
    print("Usage: python difflib-file-demo.py  file1 file2")
    sys.exit()    

def readfile(filename):
    try:
        txt = " "
        fileHandle=open(filename,'r')
        for line in fileHandle.readlines():
            txt += line
        fileHandle.close()
        print(txt)
        return txt
    except IOError as error:
        print('Read file Error:'+str(error))
        sys.exit()
   
if file1=="" or file2=="":
    print("Usage: python difflib-file-demo.py  file1 file2")
    sys.exit()  

txt1 = readfile(file1)        
txt2 = readfile(file2) 
d = difflib.Differ()
diff = d.compare(txt1.splitlines(),txt2.splitlines())
print("\n".join(list(diff)))