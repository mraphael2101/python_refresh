from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.Animal import Animal

"""
- A class that is derived from an abstract class cannot be instantiated unless
  all of its abstract methods are overridden
- An abstract method can have an implementation in the abstract class
- Even if abstract methods are implemented, designers of subclasses will be forced 
  to override the implementation
- Tip -> Abstracting code into a parent class can help increase maintainability 
"""


class Bird(Animal):

    def __init__(self, age, name):
        self.age = age
        print("Inside constructor of Bird class")

    def calculate_random_age(self) -> None:
        self.age = 3
        print('Overriden abstract method from concrete class Bird -> age {}'.format(self.age))

    # Overloading the abstract method declaration
    def generate_security_code(self, default_code=1111) -> int:
        print('Overloaded method. Security Code {}'.format(default_code))
        return default_code
