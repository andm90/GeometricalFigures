from abc import ABC, abstractmethod


class Figure(object):
    
    @abstractmethod
    def information(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


