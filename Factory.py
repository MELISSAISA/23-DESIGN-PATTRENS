import abc
import math

# Abstract Shape Class
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass

# Rectangle Class
class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

# Square Class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side

# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# ShapeFactory Class
class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            radius = self._get_positive_float("Enter the radius of the circle: ")
            return Circle(radius)
        elif name == 'rectangle':
            height = self._get_positive_float("Enter the height of the rectangle: ")
            width = self._get_positive_float("Enter the width of the rectangle: ")
            return Rectangle(height, width)
        elif name == 'square':
            side = self._get_positive_float("Enter the side length of the square: ")
            return Square(side)
        else:
            print(f"Shape '{name}' is not recognized.")
            return None

    def _get_positive_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

# Client Function
def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape (circle, rectangle, square): ").lower()

    shape = shape_factory.create_shape(shape_name)
    if shape:
        print(f"\nThe type of object created: {type(shape).__name__}")
        print(f"The area of the {shape_name} is: {shape.calculate_area():.2f}")
        print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter():.2f}")
    else:
        print("Failed to create shape. Please try again.")

# Main Execution
if __name__ == "__main__":
    shapes_client()
