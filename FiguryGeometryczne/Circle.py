import math

from Figure import Figure

class Circle(Figure):
    
    pi = math.pi
    
    def __init__(self, r):
        self.r = r
    
    def information(self):
        print("I am circle")

    def area(self):
        return Circle.pi*self.r*self.r
    
    def perimeter(self):
        return 2*Circle.pi*self.r