    
from shape import *

class Trapezium(Shape):
    
    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self.color = input("Color: ")
        self.side1 = float(input("Side1: ")) 
        self.side2 = float(input("Side2: "))
        self.side3 = float(input("Side3: "))      
        self.height = float(input("Height: "))

        print(f"{self.color} {self.shapeType} with sides {self.side1}, {self.side2} and {self.side3}, {self.side3} and height {self.height} added")
        

        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self.color , self.side1, self.side3, self.side3]})    #the list should be updated every time when person write new info
        return self.shapeList
    
    def getPerimeter(self):
        perimeter = self.side1 + self.side2 + 2 * self.side3
        return perimeter
    

    def getArea(self):
        area = (self.side1 + self.side2) * 0.6 * self.height
        return area
    

