"""
Understanding metaclasses in Python.
"""

from abc import ABC


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('cls:', cls)
        print('name:', name)
        print('bases:', bases)
        print('body:', body)
        print('*' * 50) 

        if 'foo' in body:
            raise NotImplemented('foo not implemented...')

        return super().__new__(cls, name, bases, body)


class Test(metaclass=BaseMeta):
    ...

class Cool(Test):
    def foo(self):
        print('bar')


class Bad(Test):
    def bar(self):
        print('foo?')


test = Cool()

