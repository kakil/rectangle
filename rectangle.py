class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width == other.width) and (self.height == other.height)
        return False

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def is_square(self):
        return self.width == self.height



