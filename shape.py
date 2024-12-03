class Shape:
    s_count = 0
    _color = ""

    shapeList = {}

    

    def addType(self):      #write in "program" file branch so it would open file needed
        print("(1)Rectangle (2)Triangle (3)Circle (4)Square (5)Pentagon")
        self.shape = int(input("Add: "))    #represents the type of shape as number
        self._color = input("Color: ")
        Shape.s_count += 1
        self.numberOfShape = Shape.s_count      #number of each indivisual figure
        self.shapeList.update({self.numberOfShape: [self._color , self.lenght, self.widght]})    #the list should be updated every time when person write new info
        return self.shapeList
    
    def getPerimeter(self):
        return self.edges*(self.lenght + self.widght)
    
    def getArea(self):
        self.area = self.lenght * self.widght
        return self.area

    def deleteShape(self):
        print("Which shape to remove?")
        print(self.shapeList.items())
        self.userRemoveChoice = int(input("Remove: "))
        self.shapeList.pop(self.userRemoveChoice)
        Shape.s_count = Shape.s_count - 1

    def description():
        print(f"Collection has {Shape.s_count} shapes:")

        

        


