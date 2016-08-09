# -*- coding: utf-8 -*-

"""
Adapter pattern

Client --> Adapter --> Adaptee
"""


class Man(object):

    def __init__(self):
        print "I'm a gentleman!"

    @staticmethod
    def whisper():
        print "May i have the honor to have dinner with you! "


class Ruder(object):

    def __init__(self):
        print "I'm stone broker!"

    @staticmethod
    def roar():
        print "I'll eat you baked!"


class Adapter(object):

    def __init__(self, obj, **method_mapping):
        self.obj = obj
        self.obj.__dict__.update(method_mapping)

    def __getattr__(self, item):
        return getattr(self.obj, item)


if __name__ == "__main__":
    man = Man()
    adapter = Adapter(man, speak=man.whisper)
    adapter.speak()

    ruder = Ruder()
    adapter = Adapter(ruder, speak=ruder.roar)
    adapter.speak()
