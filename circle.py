from shape import *

class Circle(Shape):
    shapeType = "Circle"

    def __init__(self, radius=0.0):
        self._radius = radius

    def addType(self):
        self.color = input("Color: ")
        self._radius = float(input("Radius: "))
        Shape.s_count += 1
        self.numberOfShape = Shape.s_count
        self.shapeList.update({self.numberOfShape: [self.color, self.shapeType, self._radius]})
        return self.shapeList

    def getPerimeter(self):
        return 2 * math.pi * self._radius

    def getArea(self):
        return math.pi * self._radius ** 2