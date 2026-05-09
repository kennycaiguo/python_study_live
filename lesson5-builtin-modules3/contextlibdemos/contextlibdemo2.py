import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print(f'__init__({how_used})')

    def __enter__(self):
        print(f'__enter__({self.how_used})')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'__exit__({self.how_used})')


@Context('这是装饰器方式')
def func(message):
    print(message)
print("---------------")
func('作为装饰器运行')


print("\n-------华丽的分割线--------\n")
with Context('上下文管理器方式'):
    print('emmmm')

