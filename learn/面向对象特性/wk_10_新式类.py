# coding: utf-8


class A(object):
    def test(self):
        print 'This is A'


class B(A):
    pass


class C(A):
    def test(self):
        print 'this is C'


class D(B,C):
    pass


d = D()
d.test()

