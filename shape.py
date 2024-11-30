class Shape:
    s_count = 0
    _color = ""

    def __init__(self, color):
        self._color = color

    def addShape(self):
        print("(1) Rectangle (2) Triangle (3) Circle (4) Square (5) Pentagon")
        self.shape = int(input("add: "))
        self.color = int(input("add"))
        self.lenght = int(input("add"))
        self.widht = int(input("add"))
        print(f"{self.color} {self.shape} with length {self.lenght} and width {self.widht} added")
