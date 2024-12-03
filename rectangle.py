from shape import *

class Rectangle(Shape):
    shapeType = "Rectangle"


    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number #Do i actually need this????
        #I can put it in program file so I 
        self.color = input("Color: ")
        self.side = float(input("Side: "))      
        self.height = float(input("Height: "))
        print(f"{self.color} Rectangle with side {self.side} and height {self.height} added")
        self.edges = 4

        super().addType     #Calls the same as what witten in base class
    
    def getPerimeter(self):
        return 2*(self.side + self.height)
    
    def getArea(self):
        return self.side * self.height * 0.5
    
    def description():
        return 
        
    
    

    