from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.Bird import Bird
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.BlackGrouse import BlackGrouse
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.HybridPheasant \
    import HybridPheasant
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.classes.HazelGrouse import HazelGrouse
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.interfaces.ICanFly \
    import InformalInterfaceICanFly
from other_tutorials.object_oriented_prog_tutorials.animals_and_behaviours_case_study.interfaces.IHop import FormalInterfaceIHop
from other_tutorials.object_oriented_prog_tutorials.inheritance_constructoroverloading_overriding.Car import Car, \
    print_base_class_method
from other_tutorials.object_oriented_prog_tutorials.inheritance_constructoroverloading_overriding.Ford import Ford


def main():
    # constructor_overloading_demo()
    # encapsulation_demo()
    # inheriting_from_an_abstract_class_and_method_overriding_and_overloading()
    # inheriting_from_a_concrete_class_and_method_overriding()
    concrete_class_method_overrides_single_informal_interface_method()
    concrete_class_method_overrides_all_formal_interface_methods()
    # multi_level_inheritance_via_classes()


def constructor_overloading_demo():
    # print_base_class_method() # function not accessible as it is not part of the inherited class

    myCar = Car('Blue')
    myCar.print_colour()
    myCar.print_colour('#F767DSG')

    myFord = Ford()  # Default Constructor
    myFord.print_colour()  # Accessing a class/static variable

    yourFord = Ford("Orange")  # Parameterised Constructor
    yourFord.print_colour('#F99999')  # Method Overriding


def encapsulation_demo():
    b_grouse = BlackGrouse(0, "Reeve")
    b_grouse.set_age(10)
    print("Reeve's age is -> " + str(b_grouse.get_age()))
    # print(b_grouse.__age)  # Throws Error -> 'BlackGrouse' object has no attribute 'age'


def inheriting_from_an_abstract_class_and_method_overriding_and_overloading():
    derived_class = Bird(1, "Mr Beaks")
    derived_class.calculate_random_age()  # Overriding an abstract method
    derived_class.generate_security_code(3333)  # Overloading an abstract method


def inheriting_from_a_concrete_class_and_method_overriding():
    reeve = BlackGrouse(0, "Reeve")
    # Has additional super() call due to multi-inheritance example
    reeve.calculate_random_age()


def multi_level_inheritance_via_classes():
    hp = HybridPheasant(2, "Aldrin")
    hp.combination_characteristics.append('Lesser Spotted Pheasant')
    print("HybridPheasant characteristics -> " + str(HybridPheasant.combination_characteristics))
    hp.calculate_random_age()
    hp.has_disorder()


def concrete_class_method_overrides_single_informal_interface_method():
    bg = BlackGrouse(2, "Spock")
    bg.ascend(0.01)
    # Returns true if the concrete class implements only some of the informal interface's methods
    print(issubclass(BlackGrouse, InformalInterfaceICanFly))
    # Lists the Superclasses of a given class by utilising Python's Method Resolution Order algorithm
    print(BlackGrouse.__mro__)


def concrete_class_method_overrides_all_formal_interface_methods():
    hg = HazelGrouse(2, "Haze")
    hg.get_average_hop_height()
    hg.get_max_hop_height()
    """
    If you don't override both methods in the Formal interface then you will get
    TypeError: Can't instantiate abstract class Eagle with abstract 
    method get_average_hop_height
    As we have overriden both methods the below statement returns true
    """
    print(issubclass(HazelGrouse, FormalInterfaceIHop))


if __name__ == "__main__":
    main()
