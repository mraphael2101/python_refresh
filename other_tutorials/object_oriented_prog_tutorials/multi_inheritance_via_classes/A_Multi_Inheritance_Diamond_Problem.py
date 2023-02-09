"""
https://python-course.eu/oop/multiple-inheritance.php
The "diamond problem" is the generally used term for an ambiguity that arises when two
classes B and C inherit from a superclass A, and another class D inherits from both B and C

If there is a method "m" in A that B or C (or even both of them) has overridden,
and furthermore, if it does not override this method, then the question is which version
of the method does D inherit?
"""


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")
        A.m(self)


class C(A):
    def m(self):
        print("m of C called")
        A.m(self)


class D(B, C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)


if __name__ == "__main__":
    x = D()
    x.m()  # Diamond Bug -> method m of A will be called twice
