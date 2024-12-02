# Asigment3
from shape import *
from circle import *
from pentagon import *
from rectangle import *
from square import *
from triangle import *

class MyExeption(Exception):
    pass
        

userChoice = None

#print(f"Collection has {Shape.s_count}")

while userChoice == None:
    try:
        userChoice = int(input("(1) Add (2) Remove (3) Shape info (4) Stats (5) Quit /n Pick option:"))

    except ValueError:
        print("Not an option")

    

