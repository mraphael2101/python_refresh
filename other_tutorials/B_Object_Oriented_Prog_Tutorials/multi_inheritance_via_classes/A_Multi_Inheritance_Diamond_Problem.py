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


def main():
    x = D()
    x.m()


if __name__ == "__main__":
    # Diamond Bug: We have to take away the call A.m(self) from m in D
    main()
