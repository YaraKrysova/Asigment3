from shape import *

class Square(Shape):
    def addType(self):
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self._color = input("Color: ")
        self.lenght = float(input("Side: "))
        self.edges = 4     
        print(f"{self._color} Square with sides {self.lenght} added")
        
        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self._color , self.lenght, self.widght]})    #the list should be updated every time when person write new info
        return self.shapeList
        