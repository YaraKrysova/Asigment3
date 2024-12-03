from shape import *

class Rectangle(Shape):
    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self._color = input("Color: ")
        self.lenght = float(input("Length: "))      
        self.widght = float(input("Width: "))
        print(f"{self._color} Rectangle with length {self.lenght} and width {self.widght} added")
        self.edges = 4

        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self._color , self.lenght, self.widght]})    #the list should be updated every time when person write new info
        return self.shapeList