from functools import reduce
from ..io import custom_error as ce

def factors(n, ordered=True):
    """Get factors of a number in a list.

    Parameters:
    n (int): The number that you want to get the factors of.
    ordered (bool): Whether you want the output to be ordered from smallest to largest. Setting this value to false will marginally increase the speed of the function. (DEFAULT: True)

    Returns:
    list: List of the factors of n.
    """
    if ordered:
        return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    else:
        return list(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Vector2: ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            ce.CustomError("TypeError").throw("Cannot add type 'Vector2' and '" + type(other).__name__ + "'.")
    
    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            ce.CustomError("TypeError").throw("Cannot subtract type 'Vector2' and '" + type(other).__name__ + "'.")
            
    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return Vector2(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        else:
            return Vector2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x // other.x, self.y // other.y)
        else:
            return Vector2(self.x // other, self.y // other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    
    