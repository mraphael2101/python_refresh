class Food:
    """
    a) The self variable is used to represent the instance of the class.
    b) Using the variable allows us to access the attributes and methods
       of the class in Python. It binds the attributes with the given arguments.
    c) The variable scope can either be at a class level or at a local method level
    """

    def __init__(self, fruit, color, size="small"):
        self.fruit = fruit
        self.color = color
        self.size = size

    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color)

    # self is also used to refer to a variable field within the class
    def get_fruit_size(self):
        return self.size


def main():
    apple = Food("apple", "red", "large")
    grapes = Food("grapes", "green")
    apple.show()
    grapes.show()
    print("Apple: " + apple.get_fruit_size())
    print("Grapes: " + grapes.get_fruit_size())


if __name__ == "__main__":
    main()
