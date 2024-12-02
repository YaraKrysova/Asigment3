# Asigment3
from shape import *
from circle import *
from pentagon import *
from rectangle import *
from square import *
from triangle import *

running = True


while running:
    userChoice = None
    shape1 = Shape()

    while userChoice == None:
        try:
            userChoice = int(input("(1) Add (2) Remove (3) Shape info (4) Stats (5) Quit /n Pick option: "))

        except ValueError:
            print("Not an option")

    if userChoice == 1:
        shape1.addType()

    elif userChoice == 2:
        shape1.deleteShape()

    elif "ESCAPE":
        break

