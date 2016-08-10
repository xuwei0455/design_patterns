# -*- coding: utf-8 -*-

"""
Bridge pattern
"""


class DressSuit(object):
    """
    ConcreteImplementor
    """
    @staticmethod
    def dress(color):
        print('Dress a {} suit'.format(color))


class DressTie(object):
    """
    ConcreteImplementor
    """
    @staticmethod
    def dress(color):
        print('Dress a {} tie'.format(color))


class Servant(object):
    """
    Refined Abstraction
    """
    def __init__(self, cloth_color, dress_handler):
        self.cloth_color = cloth_color

        self.dress_handler = dress_handler

    # low-level i.e. Implementation specific
    def dress(self):
        self.dress_handler.dress(self.cloth_color)

if __name__ == '__main__':
    servant_1 = Servant("black", DressSuit)
    servant_1.dress()

    servant_2 = Servant("red", DressTie)
    servant_2.dress()


