# Asigment3
from shape import *
from circle import *
from trapezium import *
from rectangle import *
from square import *
from triangle import *

running = ""


while running:
    userChoice = None
    shape1 = Shape()

    while userChoice == None:
        try:
            userChoice = int(input("(1) Add (2) Remove (3) Shape info (4) Stats (5) Quit /n Pick option: "))

        except ValueError:
            print("Not an option")


        #call each file in brancing like shape1= Circle(), so on
    if userChoice == 1:
        print("(1)Rectangle (2)Triangle (3)Circle (4)Square (5)Pentagon")
        shape1.addType()

    elif userChoice == 2:
        shape1.deleteShape()

    elif userChoice == 3:
        print(f"Collection has {Shape.s_count} shapes:")
        shape1.description()

    elif userChoice == 4:
        pass

    elif userChoice == 5:
        print("See you again")
        running = False

