"""
python glob module
"""
import glob

# 1.glob.glob() ->list
# print(glob.glob("./mypic/**.jpg")) # ['./mypic\\california.jpg', './mypic\\Cather-Tucker-outside-taos.jpg', './mypic\\mount_charleston_nevada_usa_photo_020.jpg', './mypic\\national-park.jpg', './mypic\\OIP.jpg', './mypic\\pinkcloud.jpg']
# print(glob.glob("../lesson3-builtin-modules1/*.py"))
"""
['../lesson3-builtin-modules1\\calendardemo.py', '../lesson3-builtin-modules1\\colloctionsdemo.py', '../lesson3-builtin-modules1\\configparserdemo.py',
 '../lesson3-builtin-modules1\\copydemo.py', '../lesson3-builtin-modules1\\datetime.datetimedemo.py', '../lesson3-builtin-modules1\\datetime.timedemo.py',
   '../lesson3-builtin-modules1\\datetimedemo.py', '../lesson3-builtin-modules1\\functoolsdemo.py', '../lesson3-builtin-modules1\\hashlibdemo.py', 
   '../lesson3-builtin-modules1\\itertoolsdemo.py', '../lesson3-builtin-modules1\\jsondemo.py', '../lesson3-builtin-modules1\\loggingdemo.py', 
   '../lesson3-builtin-modules1\\mathdemo.py', '../lesson3-builtin-modules1\\os.pathdemo.py', '../lesson3-builtin-modules1\\osdemo.py', 
   '../lesson3-builtin-modules1\\pickledemo.py', '../lesson3-builtin-modules1\\processimg.py', '../lesson3-builtin-modules1\\queuedemo.py', 
   '../lesson3-builtin-modules1\\randomdemo.py', '../lesson3-builtin-modules1\\redemo.py', '../lesson3-builtin-modules1\\shutildemo.py', 
   '../lesson3-builtin-modules1\\subprocessdemo.py', '../lesson3-builtin-modules1\\sysdemo.py', '../lesson3-builtin-modules1\\threadingdemo.py', 
   '../lesson3-builtin-modules1\\timedemo.py', '../lesson3-builtin-modules1\\uuiddemo.py', '../lesson3-builtin-modules1\\yamldemo.py']
"""
# 2.glob.iglob() ->iterator
print(glob.iglob("../lesson3-builtin-modules1/*.py")) # <generator object _iglob at 0x00000160A491C7C0>
for i in glob.iglob("../lesson3-builtin-modules1/*.py"):
    print(i)
"""
../lesson3-builtin-modules1\calendardemo.py
../lesson3-builtin-modules1\colloctionsdemo.py
../lesson3-builtin-modules1\configparserdemo.py
../lesson3-builtin-modules1\copydemo.py
../lesson3-builtin-modules1\datetime.datetimedemo.py
../lesson3-builtin-modules1\datetime.timedemo.py
../lesson3-builtin-modules1\datetimedemo.py
../lesson3-builtin-modules1\functoolsdemo.py
../lesson3-builtin-modules1\hashlibdemo.py
../lesson3-builtin-modules1\itertoolsdemo.py
../lesson3-builtin-modules1\jsondemo.py
../lesson3-builtin-modules1\loggingdemo.py
../lesson3-builtin-modules1\mathdemo.py
../lesson3-builtin-modules1\os.pathdemo.py
../lesson3-builtin-modules1\osdemo.py
../lesson3-builtin-modules1\pickledemo.py
../lesson3-builtin-modules1\processimg.py
../lesson3-builtin-modules1\queuedemo.py
../lesson3-builtin-modules1\randomdemo.py
../lesson3-builtin-modules1\redemo.py
../lesson3-builtin-modules1\shutildemo.py
../lesson3-builtin-modules1\subprocessdemo.py
../lesson3-builtin-modules1\sysdemo.py
../lesson3-builtin-modules1\threadingdemo.py
../lesson3-builtin-modules1\timedemo.py
../lesson3-builtin-modules1\uuiddemo.py
../lesson3-builtin-modules1\yamldemo.py

"""    