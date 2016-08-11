# -*- coding: utf-8 -*-

"""
Proxy pattern
"""


class WorldOutside(object):

    @staticmethod
    def access():
        print "I came out over the wall!"


class Proxy:
    def __init__(self):

        self.busy = 'No'
        self.sales = None

        self.endpoint = WorldOutside()

    def access(self):
        print "Proxy checking for endpoint availability"
        self.endpoint.access()
        print "I back in the wall!"


if __name__ == '__main__':
    p = Proxy()
    p.access()
