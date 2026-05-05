"""
multiprocess built-in module
"""
## ex1
# from multiprocessing import Process
# import time


# def fun1(name):
#     time.sleep(1)
#     print('测试%s多进程' %name)

# if __name__ == '__main__':
#     process_list = []
#     for i in range(5):
#         p = Process(target=fun1,args=('Python',))
#         p.start()
#         process_list.append(p)
#     for i in range(len(process_list)):
#          process_list[i].join()

    
#     print("Multi-Process ended ...")  

# # ex2 ok
# from multiprocessing import Process
# import time

# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name = name

#     def run(self):
#        time.sleep(1)
#        print('测试%s多进程' %self.name)     
# if __name__ == '__main__':
#     process_list = []
#     for i in range(5):
#         p = MyProcess('Python')
#         p.start()
#         process_list.append(p)
#     for i in range(len(process_list)):
#          process_list[i].join()
#     print("Multi-Process ended ...")      

# # ex3
# from multiprocessing import Process,Queue

# def fun1(q,i):
#     print(f"子进程{i+1}数据保存到队列了")
#     q.put(f"我是子进程{i+1}的数据")

# if __name__ == '__main__':
#     q = Queue()
#     proc_list=[]
#     print("保存数据到队列")
#     for i in range(8):
#         p = Process(target=fun1,args=(q,i,))    
#         p.start()
#         proc_list.append(p)

#     for p in proc_list:
#         p.join()  
#     print("==========================")    
#     print('主进程获取Queue数据')      
#     for i in range(q.qsize()):
#         print(q.get()) 
#     print("Multi-Process ended ...")     

# # ex 4 Process + Pipe   
# from multiprocessing import Process,Pipe

# def communicate(pipe):
#     print("子进程发送信息：")
#     pipe.send("你好,main进程")
#     print(f"子进程接收到信息：{pipe.recv()}")
#     pipe.close()

# if __name__ == '__main__':
#     pipe1,pipe2 = Pipe() #关键点，pipe实例化生成一个双向管
#     p = Process(target=communicate,args=(pipe2,))
#     p.start()
#     print(f"主进程接收到消息:{pipe1.recv()}")
#     print("主进程发送消息:")
#     pipe1.send("你好子进程")
#     p.join()
#     print("测试结束")

# # ex5 Manager
# # Queue和Pipe只是实现了数据交互，并没实现数据共享，即一个进程去更改另一个进程的数据。那么久要用到Managers
# from multiprocessing import Process, Manager

# def func(dic,lis,index):
#     dic[index] = 'a'
#     dic['2'] = 'b'
#     lis.append(index) 

# if __name__ == '__main__':
#     with Manager() as manager:
#         dic = manager.dict()
#         l = manager.list([])
#         proc_list = []
#         for i in range(10):
#             p = Process(target=func,args=(dic,l,i))
#             p.start()
#             proc_list.append(p)
#         for p in proc_list:
#             p.join()
#         print(dic)    
#         print(l)

## ex6 进程池 Process + Pool
# from  multiprocessing import Process,Pool
# import os, time, random

# def func(index):
#     print(f"Run Task {index+1}({os.getpid()})...")
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print(f"Task {index} consumed {end-start} seconds...")

# if __name__ == '__main__':
#     pool = Pool(5)
#     for i in range(10):
#         pool.apply_async(func=func,args=(i,))    
#     pool.close()
#     pool.join()
#     print('结束测试')

# ex7 **进程池map方法**

import os 
import PIL 

from multiprocessing import Pool 
from PIL import Image

SIZE = (75,75)
SAVE_DIRECTORY = 'thumbs'

def get_img_paths(folder):
    return (
        os.path.join(folder,f) for f in os.listdir(folder) if "jpg" in f
    )

def create_thumbnail(filePath): # 这个filePath必须是一个包含文件名的绝对路径
    image = Image.open(filePath)
    image.thumbnail(SIZE,Image.Resampling.LANCZOS)
    base,filename = os.path.split(filePath)
    savePath = os.path.join(base,SAVE_DIRECTORY,filename)
    print(savePath)
    image.save(savePath) # 注意：Iamge保存文件的时候，目标文件夹必须存在

if __name__ == '__main__':
    folder = os.path.dirname(os.path.abspath(__file__))
    src_folder = os.path.join(folder,"mypic")
    thum_dir = os.path.join(src_folder, SAVE_DIRECTORY)
    if not os.path.exists:
        print("not exist")
        os.mkdir(thum_dir)
    else:
        print("dir exists...")    

    images = get_img_paths(src_folder)
    # print(list(images))
    pool = Pool()
    pool.map(create_thumbnail, images) #关键点，images是一个可迭代对象
    pool.close()
    pool.join()
    # create_thumbnail(list(images)[1])