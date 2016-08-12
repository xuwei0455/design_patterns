# -*- coding: utf-8 -*-

"""
Command pattern

"""

from os import listdir, curdir


class ListCommand(object):

    def __init__(self, path=None):
        self.path = path or curdir

    def execute(self):
        self._list(self.path)

    @staticmethod
    def _list(path=None):
        print 'list path {} :'.format(path)
        print listdir(path)

if __name__ == "__main__":
    command = ListCommand()
    command.execute()
