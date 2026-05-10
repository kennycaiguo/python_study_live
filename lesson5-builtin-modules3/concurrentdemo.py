def curr_demo1():
    from concurrent import futures
 
    def test(num):
        import time
        return time.ctime(),num
    
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(test,1)
        print(future.result())

def curr_demo2():
    from concurrent import futures
 
    def test(num):
        import time
        return time.ctime(),num
    data = [100,200,300,400,500]
    with futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.map(test,data)
        print(list(future))


if __name__ =='__main__':
    # curr_demo1()
    curr_demo2()