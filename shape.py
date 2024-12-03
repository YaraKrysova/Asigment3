import math

class Shape:
    s_count = 0
    _color = ""
    shapeType = ""
    edges = 0       #needs for counting perimeter
    side = 0.0


    shapeList = {}

    

    def addType(self):      #write in "program" file branch so it would open file needed
        
        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self._color ,self.shapeType , self.side, self.height]})    #the list should be updated every time when person write new info
        #I hope it will see attributes
        return self.shapeList
    
    def getPerimeter(self):
        perimeter = self.edges * self.side
        return perimeter
    

    def deleteShape(self):
        print("Which shape to remove?")
        print(self.shapeList.items())
        self.userRemoveChoice = int(input("Remove: "))
        self.shapeList.pop(self.userRemoveChoice)
        Shape.s_count = Shape.s_count - 1

    def description():
        pass



        

        


