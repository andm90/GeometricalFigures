from Figure import Figure
from Rectangle import Rectangle


class Squere(Rectangle):
    

    def __init__(self, a):
        super().__init__(a, a)

    def information(self):
        print("I am squere")

    def area(self):
        return super().area()

    def perimeter(self):
        return super().perimeter()


