from collections import namedtuple


def fct_named_tuple():
    # Define a named tuple type
    Point = namedtuple('Point', ['x', 'y'])

    # Create an instance
    p = Point(10, 3)
    q = (10, 20)
    a, b = q

    print(b, a)

def sample():
    class Person:
        God = "YHWH"

        def __init__(self, name, age):
            self.father: Person | None = None
            self.__name = name
            self.age = age

        def __str(self):
            return "Mbi la so"

    p1 = Person("John", 36)

    print(p1.__name)
    print(Person.God)


def main():
    fct_named_tuple()
    print("---")


main()