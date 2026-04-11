# Task 5: Extending a Class
from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def dist(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
def main():
    a = Point(3, 4)
    b = Point(3, -4)
    c = Point(-3, 4)
    d = Point(3, -4)

    print(f'Point a: {a}')
    print(f'Point b: {b}')
    print(f'Point c: {c}')
    print(f'Point d: {d}')

    print(f'Is Point a equal to Point b? {a == b}')
    print(f'Is Point b equal to Point d? {b == d}')

    print(f'Distance between Point b and Point c: {b.dist(c)}')

    u = Vector(3, 4)
    v = Vector(3, -4)
    w = Vector(-3, 4)

    print(f'Point a: {u}')
    print(f'Point b: {v}')
    print(f'Point c: {w}')
    
    print(f'Is Vector u equal to Vector v? {u == v}')

    print(f'u + v = {u + v}')
    print(f'v + w = {v + w}')

if __name__ == '__main__':
    main()