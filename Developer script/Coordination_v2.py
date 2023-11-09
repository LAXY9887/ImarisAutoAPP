class Coordinate:

    def __init__(self,x,y) -> None:
        
        self.x = x
        self.y = y

    def get_position(self):
        return(self.x,self.y)

    def isCoordSet(self):
        if self.x > 0 and self.y > 0:
            return True
        else:
            return False

    def print_position(self):
        print("Position X = {}, Y = {}".format(self.x,self.y))

class Point(Coordinate):

    def __init__(self, x=-1, y=-1) -> None:
        super().__init__(x, y)

    def Shift(self,coordinate):
        self.x += coordinate.x
        self.y += coordinate.y

class Offset(Coordinate):

    def __init__(self, x=-1, y=-1) -> None:
        super().__init__(x, y)
