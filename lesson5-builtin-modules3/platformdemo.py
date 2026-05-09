import platform

print(platform.system())          #获取操作系统名称
print(platform.platform())        #获取操作系统名称及版本号
print(platform.version())         #获取操作系统版本号
print(platform.architecture())    #获取操作系统的位数，('32bit', 'ELF')
print(platform.machine())         #计算机类型，'i686'
print(platform.node())            #计算机的网络名称，'XF654'
print(platform.processor())       #计算机处理器信息，''i686'
print(platform.uname())
print(platform.python_build())             #python编译号(default)和日期.
print(platform.python_compiler())          #python编译器信息
print(platform.python_branch())            #python分支(子版本信息),一般为空.
print(platform.python_implementation())    #python安装履行方式,如CPython, Jython, Pypy, IronPython(.net)等
print(platform.python_revision())          #python类型修改版信息,一般为空.
print(platform.python_version())           #python版本号
print(platform.python_version_tuple()) 