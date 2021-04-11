import unittest

from Figure import Figure

class Rectangle(Figure):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def information(self):
        print("I am rectangle")

    def area(self):
        return self.a*self.b

    def perimeter(self):
        return 2*self.a + 2*self.b


        
        


