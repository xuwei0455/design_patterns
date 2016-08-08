# -*- coding: utf-8 -*-

"""
Prototype pattern

Pattern that permit clone the proto instance and do some extra
updates for the new instance.

"""


import copy


class Prototype(object):

    meta_name = "cls_a"

    def clone(self, **kwargs):
        cp = copy.deepcopy(self)
        cp.__dict__.update(**kwargs)
        return cp

if __name__ == '__main__':

    a = Prototype()
    b = a.clone(meta_name="cls_b")
    c = a.clone(extra_info="cls_c")

    print "a: ", a.meta_name
    print "b: ", b.meta_name
    print "c: ", c.meta_name
    print "c: extra ", c.extra_info
