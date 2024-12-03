from shape import *

class Square(Shape):

    shapeType = "Square"

    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self.color = input("Color: ")
        self.side = float(input("Side: "))    
        print(f"{self._color} {self.shapeType} with sides {self.side}")
        
        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self.color , self.shapeType, self.side]})    #the list should be updated every time when person write new info
        return self.shapeList
        

    
    def getPerimeter(self):
        return super().getPerimeter()

    def getArea(self):
        area = self.side * self.side
        return area
    
