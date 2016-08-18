# -*- coding: utf-8 -*-

"""
Observer patterns

'Education need not only be about furthering your career'
"""


class Subject(object):

    def __init__(self):
        self.ob = []

    def attach(self, observer):
        if observer not in self.ob:
            self.ob.append(observer)

    def detach(self, observer):
        try:
            self.ob.pop(observer)
        except ValueError:
            pass

    def receive(self, *args):
        pass


class ConcreteSubject(Subject):

    def receive(self, name):
        print "Haa, i receive a package from {}".format(name)

        if not self.ob:
            print "No observer focus on it."
        else:
            for _ob in self.ob:
                _ob.listen(name)


class Observer(object):

    def __init__(self):
        pass

    def listen(self):
        pass


class ConcreteObserver(object):

    @staticmethod
    def listen(name):
        print "I see subject receive a package names {}".format(name)

if __name__ == '__main__':
    ob1 = ConcreteObserver()
    ob2 = ConcreteObserver()

    sub = ConcreteSubject()
    sub.attach(ob1)
    sub.attach(ob2)

    sub.receive("Letter")
