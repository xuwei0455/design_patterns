# -*- coding: utf-8 -*-

"""
Strategy pattern
"""


class Fighter(object):
    """
    Context
    """
    def __init__(self, strategy):
        self.strategy = strategy

    def fly(self):
        self.strategy.fly()


class StrategyCruise(object):
    """
    Concrete Strategy
    """
    @staticmethod
    def fly():
        print "Flying with auto cruise"


class StrategySuperCruise(object):
    """
    Concrete Strategy
    """
    @staticmethod
    def fly():
        print "Flying with super cruise"


if __name__ == '__main__':
    cruise = StrategyCruise()
    super_cruise = StrategySuperCruise()

    fighter_1 = Fighter(cruise)
    fighter_2 = Fighter(super_cruise)

    fighter_1.fly()
    fighter_2.fly()
