import timeit

def clock(func):
    def clocked(*args, **kwargs):
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        run_time = timeit.default_timer() - start
        func_name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('调用>>>%s(%s)   \n返回值>>>%r   \n耗时>>>%0.8fs\n' % (func_name, arg_str, res, run_time))
        return res

    return clocked

@clock
def func(n):
    """累计加1"""
    res = 0
    for i in range(n):
        res += 1
    return res

func(100)