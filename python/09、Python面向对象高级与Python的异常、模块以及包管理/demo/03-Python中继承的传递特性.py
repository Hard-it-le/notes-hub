class C(object):
    def func(self):
        print('我是C类中的相关方法func')


class B(C):
    pass


class A(B):
    pass


a = A()
a.func()