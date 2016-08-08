# -*- coding: utf-8 -*-

"""
Singleton pattern

Design pattern that restricts the instantiation of a
class to one object.

singleton: inherit
borg: shared-state
"""


class Singleton(object):
    """
    Method 1
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_inst"):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst


class Borg(object):
    """
    Method 2
    """
    _state = {}

    def __new__(cls, *args, **kwargs):
        cls._inst = super(Borg, cls).__new__(cls, *args, **kwargs)
        cls._inst.__dict__ = cls._state
        return cls._inst


if __name__ == '__main__':
    # Method 1
    print " singleton ".join(["-"*10]*2)


    class MethodOne(Singleton):

        def __init__(self, *args, **kwargs):
            print "args: ", args
            print "kwargs: ", kwargs

    a = MethodOne("a", name="a")
    b = MethodOne("b", name="b")

    print id(a), id(b)

    # Method 2
    print " borg ".join(["-" * 10] * 2)


    class MethodTwo(Borg):

        def __init__(self, *args, **kwargs):
            print "args: ", args
            print "kwargs: ", kwargs

    a = MethodTwo("a", name="a")
    b = MethodTwo("b", name="b")

    a.state = "init"
    print "a.state: ", a.state
    b.state = "produce"
    print "b.state: ", b.state

    print id(a.__dict__), id(b.__dict__)
    print id(a), id(b)

