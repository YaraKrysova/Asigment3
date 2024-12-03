from shape import *

class Rectangle(Shape):
    shapeType = "Rectangle"


    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number #Do i actually need this????
        #I can put it in program file so I can make branching
        #I'll do it after writing all child classes
        self.color = input("Color: ")
        self.side = float(input("Widht: "))      
        self.height = float(input("Lenght: "))
        print(f"{self.color} {self.shapeType} with with sides {self.side} and lenght {self.height}")
        self.edges = 4

        super().addType     #Calls the same as what witten in base class
    
    def getPerimeter(self):
        perimeter = 2*(self.side + self.height)
        return perimeter
    
    def getArea(self):
        area = self.side * self.height * 0.5
        return area
    

    
    
        
    
    

    