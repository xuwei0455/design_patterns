# -*- coding: utf-8 -*-

"""
Builder pattern


"""


class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_fridge()
        self.builder.build_main()
        self.builder.build_box()

    def get_building(self):
        return self.builder.fridge


class Builder(object):
    """
    Abstract Builder
    """
    def __init__(self):
        self.fridge = None

    def new_fridge(self):
        self.fridge = Fridge()

    def build_main(self):
        raise NotImplementedError

    def build_box(self):
        raise NotImplementedError


# Concrete Builder
class BuilderBig(Builder):

    def build_main(self):
        self.fridge.main = 'Big'

    def build_box(self):
        self.fridge.box = 'Big'


class BuilderSmall(Builder):

    def build_main(self):
        self.fridge.main = 'Little'

    def build_box(self):
        self.fridge.box = 'Little'


class Fridge(object):
    """
    Product
    """
    def __init__(self):
        self.main = None
        self.box = None

    def __repr__(self):
        return 'Fridge: {0.main} in Box: {0.box}'.format(self)


if __name__ == "__main__":
    director = Director()
    director.builder = BuilderBig()
    director.construct_building()
    building = director.get_building()
    print(building)

    director.builder = BuilderSmall()
    director.construct_building()
    building = director.get_building()
    print(building)




