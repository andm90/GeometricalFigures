from Figure import Figure
from Circle import Circle
from Rectangle import Rectangle
from Squere import Squere


if __name__ == "__main__":
    print("Hello World")

    circle = Circle(5)
    rectangle = Rectangle(2,3)
    squere = Squere(5)

    figures = [circle, rectangle, squere]

    for name in figures:
        name.information()

    for area in figures:
        print(area.area())

    for perimeter in figures:
        print(perimeter.perimeter())