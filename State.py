# -*- coding: utf-8 -*-

"""
State pattern
"""


class State(object):

    """
    State
    """
    states = {}

    def __new__(cls, *args, **kwargs):
        if cls not in State.states:
            State.states[cls] = super(State, cls).__new__(cls, *args, **kwargs)
        obj = State.states[cls]
        return obj

    def __init__(self, screen):
        self.screen = screen

    def switch(self):
        for _cls, status in State.states.iteritems():
            if self.screen.status != status:
                self.screen.status = status
                break


class LandscapeMode(State):

    """
    Concrete State
    """
    @staticmethod
    def show():
        print "***********"
        print "*         *"
        print "***********"


class PortraitMode(State):

    """
    Concrete State
    """
    @staticmethod
    def show():
        print "********"
        print "*      *"
        print "*      *"
        print "*      *"
        print "********"


class Screen(object):

    def __init__(self):
        self.landscape = LandscapeMode(self)
        self.portrait = PortraitMode(self)

        self.status = self.landscape

    def display(self):
        self.status.show()

    def switch(self):
        self.status.switch()


if __name__ == '__main__':
    display = Screen()
    display.display()

    display.switch()
    display.display()

    display.switch()
    display.display()

    display.switch()
    display.display()
