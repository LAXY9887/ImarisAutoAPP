class Point:

    def __init__(self,x=-1,y=-1) -> None:
        self.x = x
        self.y = y
        
    def setPoint(self,newX,newY):
        self.x = newX
        self.y = newY

    def getPoint(self):
        return self

    def isSet(self):
        if self.x > 0 and self.y > 0:
            return True
        else:
            return False

    def showPoint(self):
        return (self.x,self.y)

if __name__ == "__main__":
    print("Record of coordinate")