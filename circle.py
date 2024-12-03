from shape import *

class Circle(Shape):
    _radius: 0.0

    #def __init__(self, radius):
       #self._radius = radius 

    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self._color = input("Color: ")
        self._radius = int(input("Radius: "))

        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self._color , self.lenght, self.widght]})    #the list should be updated every time when person write new info
        return self.shapeList
