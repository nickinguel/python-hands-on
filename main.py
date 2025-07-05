from collections import namedtuple


def fct_named_tuple():
    # Define a named tuple type
    Point = namedtuple('Point', ['x', 'y'])

    # Create an instance
    p = Point(10, 3)
    q = (10, 20)
    a, b = q

    print(b, a)


fct_named_tuple()
