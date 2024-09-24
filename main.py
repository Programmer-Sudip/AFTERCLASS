class Polygon:
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius * self.radius

# Example usage
triangle = Triangle(10, 5)
rectangle = Rectangle(10, 5)
square = Square(4)
circle = Circle(7)

print(f"Area of Triangle: {triangle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")
print(f"Area of Square: {square.area()}")
print(f"Area of Circle: {circle.area()}")
