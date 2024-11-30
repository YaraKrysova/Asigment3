class Shape:
    s_count = 0
    _color = ""

    shapeList = {}

    #def __init__(self, color):
        #self._color = color

    def addType(self):
        print("(1)Rectangle (2)Triangle (3)Circle (4)Square (5)Pentagon")
        self.shape = int(input("Add: "))
        self._color = input("Color: ")
        self.lenght = float(input("Length: "))       #Overwrite method in child class
        self.widht = float(input("Width: "))
        
        if self.shape == 1:
            print(f"{self._color} Rectangle with length {self.lenght} and width {self.widht} added")
        
        elif self.shape == 2:
            print(f"{self._color} Triangle with length {self.lenght} and width {self.widht} added")
        
        elif self.shape == 3:
            print(f"{self._color} Circle with length {self.lenght} and width {self.widht} added")
        
        elif self.shape == 4:
            print(f"{self._color} Square with length {self.lenght} and width {self.widht} added")
        
        elif self.shape == 5:
            print(f"{self._color} Pentagon with length {self.lenght} and width {self.widht} added")
        
        
        Shape.s_count += 1
        self.shapeList.update({self.shape: [self._color , self.lenght, self.widht]})

    

    def desription():
        print(f"Collection has {Shape.s_count} shapes:")

        


shape1 = Shape()
shape1.addType()