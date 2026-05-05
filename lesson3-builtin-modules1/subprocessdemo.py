"""
subprocess module
subprocess.call([cmd,param]) # execute the cmd and ret the result plus a status code
subprocess.run([cmd,param]) # execute the cmd and ret the result plus a  CompletedProcess object
subprocess.check_call([cmd,param]) # the same like call
sp.check_output(["node","-v"]) # get the output of the cmd only(byte sequence),no status code
sp.getoutput(["node","-v"]) # get the output of the cmd but in string format
sp.getstatusoutput(["notepad"]) # return a tuple (0, ''),0 means successful
"""
import subprocess as sp

# call
# usage #1
# print(sp.call(["node","-v"])) # v18.20.8  0 one value not two
# ret = sp.call(["node","-v"]) # v18.20.8  0
# print(ret)  # "v18.20.8\n 0"
# sp.call(["notepad"]) # the param is optional
# usage #2
# print(sp.call("dir",shell=True))
# print(sp.call("mspaint",shell=True))

# run
# print(sp.run("dir",shell=True))
# print(sp.run(["node","-v"])) # v18.20.8 CompletedProcess(args=['node', '-v'], returncode=0)

# check_call
# ret = sp.check_call(["node","-v"])
# print(ret)

# print(sp.check_output(["node","-v"])) # b'v18.20.8\r\n'
# print(sp.getoutput(["node","-v"])) # v18.20.8

# print(sp.getstatusoutput(["notepad"])) # (0, '')
# print(sp.Popen(["notepad"])) # <Popen: returncode: None args: ['notepad']>
# print(sp.Popen(["node","-v"])) #  v18.20.8