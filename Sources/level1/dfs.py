class A:
    def __init__(self):
        print('init')

def foo(self):
    print('foo')

A.foo = foo

a = A()
a.foo()