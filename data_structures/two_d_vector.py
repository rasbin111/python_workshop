"""

Addition
>>> v1 = Vector(3,4)
>>> v2 = Vector(4,3)
>>> v3 = v1 + v2
Vector(7, 7)

Absolute value
>>> v = Vector(3,4)
>>> abs(v)
5.0

Scalar multiplication
>>> v*3
Vector(9, 12)
>>> abs(v*3)
15.0

""" 

import math

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
        # return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, multiplier):
        return Vector(self.x*multiplier, self.y*multiplier)


    


if __name__=="__main__":
    import doctest
    doctest.testmod()
