# -*- coding: utf-8 -*-

"""
Decorator pattern
"""

from functools import wraps


def decorator(fn):
    @wraps(fn)
    def wrap(name):
        print "Run before func <{}>".format(fn.__name__)
        fn(name)
    return wrap


@decorator
def component(name):
    print "I'm a concrete component names: {}".format(name)

if __name__ == '__main__':
    component("faith")