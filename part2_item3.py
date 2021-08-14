class Shape:
    """
    Contains method for computing area.
    """
    area = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        """Computation for area of quadrilateral"""
        raise NotImplementedError


class Square(Shape):
    """Computation for area of square"""
    def __init__(self, length):
        super().__init__(length, width=length)

    def get_area(self):
        self.area = self.length * self.width
        return self.area


if __name__ == '__main__':
    sqr = Square(5)
    print(sqr.get_area())
