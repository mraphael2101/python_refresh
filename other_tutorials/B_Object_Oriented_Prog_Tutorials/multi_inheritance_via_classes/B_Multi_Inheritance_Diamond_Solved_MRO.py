"""
The question arises about how the super functions makes decisions.
How does it decide which class has to be used? As we have already
mentioned, it uses the so-called method resolution order(MRO). It
is based on the "C3 superclass linearisation" algorithm. This is
called a linearisation, because the tree structure is broken down
into a linear order
"""


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")
        super().m()


class C(A):
    def m(self):
        print("m of C called")
        super().m()


class D(B, C):
    def m(self):
        print("m of D called")
        super().m()


if __name__ == "__main__":
    # A clean solution to the Diamond problem (Redundant call is removed)
    D().m()
    # C().m()
    # B().m()
    # A().m()
