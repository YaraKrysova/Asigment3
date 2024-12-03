from shape import *

class Rectangle(Shape):
    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self._color = input("Color: ")
        self.lenght = float(input("Length: "))      
        self.widght = float(input("Width: "))
        print(f"{self._color} Triangle with length {self.lenght} and width {self.widght} added")
        self.edges = 4