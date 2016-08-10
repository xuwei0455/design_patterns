# -*- coding: utf-8 -*-

"""
Facade patterns
"""


class Power(object):
    """
    SubSystem
    """
    @staticmethod
    def start():
        print "Power on!"


class Display(object):
    """
    Subsystem
    """
    @staticmethod
    def start():
        print "Display on!"


class Client(object):
    """
    Facade
    """
    def __init__(self):
        self.power = Power()
        self.display = Display()
        self.components = [self.power, self.display]

    def start_all(self):
        for _component in self.components:
            _component.start()


if __name__ == '__main__':
    client = Client()
    client.start_all()
