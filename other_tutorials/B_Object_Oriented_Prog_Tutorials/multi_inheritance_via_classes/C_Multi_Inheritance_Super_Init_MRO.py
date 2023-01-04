class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()


"""
Typically, the super function is often used when instances are initialized with 
the __init__ method.
Uncomment the code line by line and examine the output to better understand the
sequence of constructor calls.
"""

if __name__ == "__main__":
    d = D()
    # c = C()
    # b = B()
    # a = A()

