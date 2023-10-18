class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @staticmethod
    def is_square(width, height):
        return width == height

    @classmethod
    def create_square(cls, side_length):
        return cls(side_length, side_length)

    @staticmethod
    def is_positive_number(value):
        try:
            number = float(value)
            return number > 0
        except ValueError:
            return False

def input_number(prompt):
    while True:
        value = input(prompt)
        if Rectangle.is_positive_number(value):
            return float(value)
        else:
            print("Введите полож число")

width = input_number("Введите шириную прямоугольника: ")
height = input_number("Введите высоту прям: ")
rectangle = Rectangle(width, height)
print("Площадь прям:", rectangle.calculate_area())
print("Это квад?", Rectangle.is_square(rectangle.width, rectangle.height))
