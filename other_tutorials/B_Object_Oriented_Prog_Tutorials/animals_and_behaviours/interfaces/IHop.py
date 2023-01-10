import abc

"""
A class that does not implement any methods at all and simply tells us what the
class should do but provides no advice on how to do it, is known as an interface

Formal interfaces are to be used for large applications to enforce the subclass 
instantiation of abstract methods, you’ll utilise Python’s built-in ABCMeta 
from the abc module

When designing the interface, imagine you are the object and that you have a 
very strong preference for privacy
"""


class FormalInterfaceIHop(abc.ABC):
    """
    A formal interface will raise errors when the abstract methods
    aren’t overridden
    Note that the interface itself cannot be instantiated, which means
    that we cannot create an object of the interface
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        """
        Subclass detection mechanism:
        Returns true if the subclass overrides all methods within the
        formal interface
        :param subclass:
        :return: boolean
        """
        return (hasattr(subclass, 'get_average_hop_height') and
                callable(subclass.get_average_hop_height) and
                hasattr(subclass, 'get_max_hop_height') and
                callable(subclass.get_max_hop_height) or
                NotImplemented)

    @abc.abstractmethod
    def get_average_hop_height(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_max_hop_height(self) -> float:
        raise NotImplementedError
