class Person:
    """
    This class represents an individual with personal information.

    Attributes:
    - first_name (str): First name of the person.
    - last_name (str): Last name of the person.
    - address (str): Address of the person.

    Class Variables:
    - list_all (list): A list containing all instances of Person.

    Methods:
    - __init__: Initializes a Person object with first_name, last_name, and address.
    - listall: Prints details of all instances of Person.
    """

    # Class variable to store all instances of Person
    list_all = []

    def __init__(self, first_name: str, last_name: str, address: str):
        """
        Initializes a Person object with provided personal information.

        :param first_name: First name of the person.
        :param last_name: Last name of the person.
        :param address: Address of the person.
        """
        assert len(first_name) > 0, f"First name {first_name} cannot be zero length."
        assert len(last_name) > 0, f"last name {last_name} cannot be zero length."
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        Person.list_all.append(self)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        self.__address = value

    @classmethod
    def listall(cls):
        """Class method to print details of all instances of Person."""
        for a in Person.list_all:
            print(a.__class__, a.__dict__)


if __name__ == '__main__':
    person1 = Person('John', 'Doe', '123 Main St')
    person2 = Person('Alice', 'Smith', '456 Elm St')

    print(person1.last_name)
