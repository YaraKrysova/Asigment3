# Asigment3
from shape import *
from circle import *
from trapezium import *
from rectangle import *
from square import *
from triangle import *


class Program:
    shape1 = Shape()
    rectangle1 = Rectangle(1)
    trapezium1 = Trapezium(2)
    circle1 = Circle(3)
    square1 = Square(4)
    triangle1 = Triangle(5)

    def run(self):
        running = True
        while running:
            userChoice = None
            

            while userChoice == None:
                try:
                    userChoice = int(input("(1) Add (2) Remove (3) Shape info (4) Stats (5) Quit /n Pick option: "))

                except ValueError:
                    print("Not an option")


                #call each file in brancing like circle1= Circle(), so on
            if userChoice == 1:
                print("(1)Rectangle (2)Triangle (3)Circle (4)Square (5)Trapezium")
                self.shape1.addType()

            elif userChoice == 2:
                self.shape1.deleteShape()

            elif userChoice == 3:
                self.shape1.description()
                if userChoice == "Escape":
                    pass
                
                


            elif userChoice == 4:
                self.shape1.displayInfo()

                
            elif userChoice == 5:
                print("See you again")
                running = False

prog = Program()
prog.run()