import contextlib

@contextlib.contextmanager
def make_context():
    print("enter make_context")
    try:
        yield {}
    except RuntimeError as err:
        print(f"{err=}")

print("Normal")
with make_context() as value:
    print("in with")

print("RuntimeError")
with make_context() as value:
    raise RuntimeError("runtimeerror")

print("Else Error")
with make_context() as value:
    raise ZeroDivisionError("0 不能作为分母")
