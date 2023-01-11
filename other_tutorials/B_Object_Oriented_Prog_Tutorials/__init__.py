from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.Bird import Bird
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.BlackGrouse import BlackGrouse
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.HybridPheasant \
    import HybridPheasant
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.classes.HazelGrouse import HazelGrouse
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.interfaces.ICanFly \
    import InformalInterfaceICanFly
from other_tutorials.B_Object_Oriented_Prog_Tutorials.animals_and_behaviours.interfaces.IHop import FormalInterfaceIHop
from other_tutorials.B_Object_Oriented_Prog_Tutorials.inheritance_constructoroverloading_overriding.Car import Car, \
    print_base_class_method
from other_tutorials.B_Object_Oriented_Prog_Tutorials.inheritance_constructoroverloading_overriding.Ford import Ford


def main():
    # inheriting_from_a_concrete_class_method_overriding_constructor_overloading()
    inheriting_from_a_concrete_class_and_method_overriding()
    # inheriting_from_an_abstract_class_and_method_overriding()
    # concrete_class_method_overrides_single_informal_interface_method()
    # concrete_class_method_overrides_all_formal_interface_methods()
    # multi_level_inheritance_via_classes()


def inheriting_from_a_concrete_class_method_overriding_constructor_overloading():
    # print_base_class_method() # function not accessible as it is not part of the inherited class

    myCar = Car('Blue')
    myCar.print_colour()
    myCar.print_colour('#F767DSG')

    myFord = Ford()  # Default Constructor
    myFord.print_colour()  # Accessing a class/static variable

    yourFord = Ford("Orange")  # Parameterised Constructor
    yourFord.print_colour('#F99999')  # Method Overriding


def inheriting_from_an_abstract_class_and_method_overriding():
    derived_class = Bird(1, "Mr Beaks")
    derived_class.calculate_random_age()  # Overriding an abstract method
    derived_class.generate_security_code(3333)  # Overloading an abstract method


def inheriting_from_a_concrete_class_and_method_overriding():
    b_spar = BlackGrouse(0, "Reeve")
    # Has additional super() call due to multi-inheritance example
    b_spar.calculate_random_age()


def multi_level_inheritance_via_classes():
    cb = HybridPheasant(2, "Aldrin")
    cb.combination_characteristics.append('Lesser Spotted Pheasant')
    print("HybridPheasant characteristics -> " + str(HybridPheasant.combination_characteristics))
    cb.calculate_random_age()
    cb.has_disorder()


def concrete_class_method_overrides_single_informal_interface_method():
    bs = BlackGrouse(2, "Spock")
    bs.ascend(0.01)
    # Returns true if the concrete class implements only some of the informal interface's methods
    print(issubclass(BlackGrouse, InformalInterfaceICanFly))
    # Lists the Superclasses of a given class by utilising Python's Method Resolution Order algorithm
    print(BlackGrouse.__mro__)


def concrete_class_method_overrides_all_formal_interface_methods():
    ea = HazelGrouse(2, "Haze")
    ea.get_average_hop_height()
    ea.get_max_hop_height()
    """
    If you don't override both methods in the Formal interface then you will get
    TypeError: Can't instantiate abstract class Eagle with abstract 
    method get_average_hop_height
    As we have overriden both methods the below statement returns true
    """
    print(issubclass(HazelGrouse, FormalInterfaceIHop))


if __name__ == "__main__":
    main()
