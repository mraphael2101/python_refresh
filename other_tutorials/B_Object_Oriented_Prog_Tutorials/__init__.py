from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.Bird import Bird
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.BlackSparrow import BlackSparrow
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.CrossBread import CrossBread
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.Eagle import Eagle
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.ICanFly import InformalInterfaceICanFly
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.IHop import FormalInterfaceIHop
from other_tutorials.B_Object_Oriented_Prog_Tutorials.inheritance_constructoroverloading_overriding.Car import Car, print_base_class_method
from other_tutorials.B_Object_Oriented_Prog_Tutorials.inheritance_constructoroverloading_overriding.Ford import Ford

"""
Examples of:
 - Inheritance and Multi-Level Inheritance via Classes,
 - Informal and Formal Interfaces,
 - Method Overriding,
 - Method Overloading,
 - Constructor Overloading
"""

def main():
    inheriting_from_an_abstract_class_and_method_overriding()
    inheriting_from_a_concrete_class_and_method_overriding()
    inheriting_from_a_concrete_class_method_overriding_constructor_overloading()
    multi_level_inheritance_via_classes()
    concrete_class_method_overrides_single_informal_interface_method()
    concrete_class_method_overrides_all_formal_interface_methods()


def inheriting_from_a_concrete_class_method_overriding_constructor_overloading():
    myCar = Car('Blue')
    myCar.print_colour('#F767DSG')
    print(myCar.driving_mode)

    myFord = Ford("Orange")         # Parameterised Constructor
    myFord.print_colour('#F99999')  # Method Overriding

    myFord2 = Ford()                # Default Constructor
    print(myFord2.driving_mode)     # Accessing a class variable
    print_base_class_method()       # Inherited Base class method


def inheriting_from_an_abstract_class_and_method_overriding():
    derived_class = Bird(1, "Mr Beaks")
    derived_class.calculate_random_age()  # Overriding an abstract method
    derived_class.generate_security_code(3333)  # Overloading an abstract method


def inheriting_from_a_concrete_class_and_method_overriding():
    b_spar = BlackSparrow(0, "Mr Sparrow")
    # Has additional super() call due to multi-inheritance example
    b_spar.calculate_random_age()


def multi_level_inheritance_via_classes():
    # https://python-course.eu/oop/multiple-inheritance.php
    cb = CrossBread(2, "Mr Sweets")
    cb.calculate_random_age()


def concrete_class_method_overrides_single_informal_interface_method():
    bs = BlackSparrow(2, "Mr Sparrow")
    bs.ascend(0.01)
    # Returns true if the concrete class implements only some of the informal interface's methods
    print(issubclass(BlackSparrow, InformalInterfaceICanFly))
    # Lists the Superclasses of a given class by utilising Python's Method Resolution Order algorithm
    print(BlackSparrow.__mro__)


def concrete_class_method_overrides_all_formal_interface_methods():
    ea = Eagle(2, "Mr Hawks")
    ea.get_average_hop_height()
    ea.get_max_hop_height()
    """
    If you don't override both methods in the Formal interface then you will get
    TypeError: Can't instantiate abstract class Eagle with abstract 
    method get_average_hop_height
    As we have overriden both methods the below statement returns true
    """
    print(issubclass(Eagle, FormalInterfaceIHop))


if __name__ == "__main__":
    main()

