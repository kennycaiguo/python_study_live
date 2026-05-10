def asyncio_demo1():
    import asyncio

    # 定义一个简单的异步函数
    async def my_coroutine(name):
        print(f"任务 {name} 开始执行")
        await asyncio.sleep(1)  # 模拟任务的延时
        print(f"任务 {name} 完成")

    # 获取事件循环
    loop = asyncio.get_event_loop()

    print("任务创建之前")

    # 创建任务并加入事件循环
    task = loop.create_task(my_coroutine("A"))
    print("任务创建之后，任务已加入事件循环")

    # 运行事件循环，直到任务完成
    loop.run_until_complete(task)

    # 关闭事件循环
    loop.close()

    print("事件循环已关闭")

def asyncio_demo2():
    import asyncio

    # 异步任务1: 打印任务开始、等待1秒并打印任务完成
    async def task_completed():
        print("任务1正在执行")
        await asyncio.sleep(1)  # 模拟异步操作，暂停1秒
        print("任务1完成")

    # 异步任务2: 打印任务开始、等待2秒并打印任务完成
    async def task_cancelled():
        print("任务2正在执行")
        await asyncio.sleep(2)  # 模拟异步操作，暂停2秒
        print("任务2完成")

    # 主异步函数
    async def main():
        # 创建并启动两个异步任务
        task1 = asyncio.create_task(task_completed())  # 创建任务1
        task2 = asyncio.create_task(task_cancelled())  # 创建任务2

        # 等待task1任务完成
        await task1

        # 取消task2任务
        task2.cancel()  # 此时调用cancelled()就会返回True
        
        # 异常处理: 捕获任务2被取消的异常
        try:
            await task2  # 尝试等待task2完成
        except asyncio.CancelledError:
            # 如果task2被取消
            pass

        # 检查task1是否完成
        if task1.done():
            print("任务1已完成")

        # 检查task2是否被取消
        if task2.cancelled():
            print("任务2已取消")
        else:
            print("任务2已完成")    

    # 运行主异步函数
    asyncio.run(main())  # 启动事件循环，执行main函数

def asyncio_demo3():
    import asyncio

    # 定义一个协程，模拟异常
    async def faulty_coroutine():
        raise ValueError("协程中发生了错误。")

    # 主程序
    async def main():
        # 创建协程任务
        task = asyncio.create_task(faulty_coroutine())
        
        # 等待任务执行完成，捕获异常
        try:
            await task
        except Exception as e:
            # 获取任务中的异常
            exception = task.exception()
            print(f"任务异常: {exception}")

    # 运行事件循环
    asyncio.run(main())

def asyncio_demo4():
    import asyncio

    # 异步任务1: 打印任务开始、等待1秒并打印任务完成
    async def task_completed():
        print("任务1正在执行")
        await asyncio.sleep(1)  # 模拟异步操作，暂停1秒
        print("任务1完成")

    # 异步任务2: 打印任务开始、等待2秒并打印任务完成
    async def task_cancelled():
        print("任务2正在执行")
        await asyncio.sleep(2)  # 模拟异步操作，暂停2秒
        print("任务2完成")

    # 定义完成回调函数
    def task_complete_cb(task):
        print(f"恭喜，任务:{task} 圆满完成...")

    # 主异步函数
    async def main():
        # 创建并启动两个异步任务
        task1 = asyncio.create_task(task_completed())  # 创建任务1
        task2 = asyncio.create_task(task_cancelled())  # 创建任务2

        task1.add_done_callback(task_complete_cb)
        task2.add_done_callback(task_complete_cb)
        # 等待task1任务完成
        await task1

        # 取消task2任务
        task2.cancel()  # 此时调用cancelled()就会返回True
        
        # 异常处理: 捕获任务2被取消的异常
        try:
            await task2  # 尝试等待task2完成
        except asyncio.CancelledError:
            # 如果task2被取消
            pass

        # 检查task1是否完成
        if task1.done():
            print("任务1已完成")

        # 检查task2是否被取消
        if task2.cancelled():
            print("任务2已取消")
        else:
            print("任务2已完成")    

    # 运行主异步函数
    asyncio.run(main())  # 启动事件循环，执行main函数    

if __name__ == '__main__':
    # asyncio_demo1()    
    # asyncio_demo2()    
    # asyncio_demo3()    
    asyncio_demo4()    
