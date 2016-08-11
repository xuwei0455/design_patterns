# -*- coding: utf-8 -*-

"""
Flyweight pattern
"""

import weakref


class Letter(object):

    _pool = weakref.WeakValueDictionary()

    def __new__(cls, character, *args, **kwargs):
        key = character.lower()
        instance = cls._pool.get(key)
        if not instance:
            instance = object.__new__(cls, *args, **kwargs)
            cls._pool[key] = instance
        return instance

    def __init__(self, character, color="Black"):
        self.color = color


if __name__ == '__main__':
    a = Letter("a")
    print len(Letter._pool)
    print a.color
    A = Letter("A", color="Red")
    print len(Letter._pool)
    print a.color, A.color

    print id(a) == id(A)
    print id(a.color) == id(A.color)

    print len(Letter._pool)
    del a
    print len(Letter._pool)
    del A
    print len(Letter._pool)
