from shape import *

class Rectangle(Shape):

    shapeType = "Triangle"

    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self.color = input("Color: ")
        self.side = float(input("Side: "))      
        self.height = float(input("Height: "))
        print(f"{self._color} Triangle with side {self.side} and height {self.height} added")
        self.edges = 3

    def getPerimeter(self):
        return super().getPerimeter()
    
    def getArea(self):
        area = 0.5 * self.side 
        return area