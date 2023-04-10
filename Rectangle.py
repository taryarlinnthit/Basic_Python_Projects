# Written by Taryarlinnthit 4/10/2023
class Rectangle:
    def __init__(self, length, width):
        assert length > 0, f"The length {length} is not greater than 0"
        assert width > 0, f"The width {width} is not greater than 0"

        self.length = length
        self.width = width

    # calculating area
    def area(self):
        area = self.length * self.width
        return area

    # calculating perimeter
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    # printing area and perimeter
    def providing_info(self):
        print(f"The area of the rectangle is {self.area()}")
        print(f"The perimeter is {self.perimeter()}")


lth = int(input("Enter length:"))
wth = int(input("Enter width:"))

problem = Rectangle(lth, wth)
problem.providing_info()
