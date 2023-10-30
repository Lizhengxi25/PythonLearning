class A(object):

    def __init__(self):
        self.n = 2

    def add(self, m):
        print("In A now, The self is {}.".format(self), "which is {}".format(self.n))
        self.n += m
        print("After add, in A now, The self is {},".format(self), "which is {}".format(self.n))

class B(A):

    def __init__(self):
        self.n = 3

    def add(self, m):
        print("In B now, the self is {}.".format(self), "which is {}".format(self.n))
        super().add(m)
        self.n += 3
        print("After add, in B now, The self is {},".format(self), "which is {}".format(self.n))

class C(A):

    def __init__(self):
        self.n = 4

    def add(self, m):
        print("In C now, the self is {}.".format(self), "which is {}".format(self.n))
        super().add(m)
        self.n += 4
        print("After add, in C now, The self is {},".format(self), "which is {}".format(self.n))

class D(B, C):

    def __init__(self):
        self.n = 5

    def add(self, m):
        print("In D now, the self is {},".format(self), "which is {}".format(self.n))
        super(D, self).add(m)
        self.n += 5
        print("After add, in D now, The self is {},".format(self), "which is {}".format(self.n))
