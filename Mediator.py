# -*- coding: utf-8 -*-

"""
Mediator pattern
"""


class AbstractColleague(object):
    """
    AbstractColleague
    """

    def __init__(self, mediator):
        self.mediator = mediator


class ConcreteColleague(AbstractColleague):
    """
    ConcreteColleague
    """
    def __init__(self, name, mediator):
        self.name = name
        AbstractColleague.__init__(self, mediator)

    def send(self, message, receiver=None):
        self.mediator.send(message, self, receiver)

    @staticmethod
    def notify(name, message, sender):
        print u'From: {} To: {} -- {}'.format(name, sender.name, message)


class AbstractMediator(object):
    """
    AbstractMediator
    """
    def send(self, message, colleague):
        pass


class ConcreteMediator(AbstractMediator):

    def __init__(self, name):
        self.name = name

        self.colleagues = []

    def register(self, colleague):
        self.colleagues.append(colleague)

    def send(self, message, colleague, receiver=None):
        if receiver:
            receiver.notify(colleague.name, message, receiver)
        else:
            for _ in self.colleagues:
                if _ != colleague:
                    _.notify(colleague.name, message, _)


if __name__ == '__main__':
    mediator = ConcreteMediator(u'UN')

    USA = ConcreteColleague(u'USA', mediator)
    mediator.register(USA)
    Japan = ConcreteColleague(u'Japan', mediator)
    mediator.register(Japan)
    Iraq = ConcreteColleague(u'Iraq', mediator)
    mediator.register(Iraq)
    UK = ConcreteColleague(u'UK', mediator)
    mediator.register(UK)

    USA.send(u"I'm the boss, bitch！")
    Japan.send(u'Emm...', receiver=USA)
    Iraq.send(u'A ha!', receiver=USA)
    UK.send(u"Reversed?")
    UK.send(u"My litter brother send that, boss...Trust me!", receiver=USA)
