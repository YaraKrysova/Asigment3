import math


class Shape:
    s_count = 0
    deletedShapes = 0
    shapeList = {}

    def addType(self):
        Shape.s_count += 1
        self.numberOfShape = Shape.s_count
        return self.shapeList

    def deleteShape(self):
        print("Which shape to remove?")
        print(self.shapeList.items())
        userRemoveChoice = int(input("Remove: "))
        if userRemoveChoice in self.shapeList:
            self.shapeList.pop(userRemoveChoice)
            Shape.deletedShapes += 1
            print(f"Shape {userRemoveChoice} removed.")
        else:
            print("Invalid choice.")

    def description(self):
        print(f"Collection has {Shape.s_count} shapes:")
        for key, value in self.shapeList.items():
            print(f"{key}: {value}")

    def displayInfo(self):
        print(f"Total shapes created: {Shape.s_count}")
        print(f"Shapes currently in collection: {len(self.shapeList)}")
        print(f"Shapes removed from collection: {Shape.deletedShapes}")




        

        


