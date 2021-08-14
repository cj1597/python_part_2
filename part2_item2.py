import math


class Circle:
    """
    Contains methods for area of circle.
    """
    def __init__(self, radius):
        self.radius = float(radius)

    def get_area(self):
        """
        Compute for area of circle with radius as input.
        """
        try:
            area = math.pi * self.radius ** 2
            return f'Area = {area}'
        except ValueError:
            return "Enter a valid number!"


circle = Circle(5)
print(circle.get_area())
