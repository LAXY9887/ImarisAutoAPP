from GUI_Coordination import Point

class PannedWindowManager:

    def __init__(self,Initial_coord,offset,windowObj,parent) -> None:
        self.Initial_coord = Initial_coord
        self.offset = offset
        self.coord_list = [self.Initial_coord]
        self.pannedWindow_list = []
        self.windowObj = windowObj
        self.parent = parent

    def PlaceWindow(self):

        # Calculate new point
        lp = self.coord_list[len(self.coord_list)-1]

        # Generate new label
        newOne = self.windowObj(lp,parentPage=self.parent,manager=self)
        self.pannedWindow_list.append(newOne)

        # offset
        lp = Point(lp.x+self.offset.x,lp.y+self.offset.y)
        if lp not in self.coord_list:
            self.coord_list.append(lp)

    def updateWindow(self):
        for i in range(len(self.coord_list)-1):
            window = self.pannedWindow_list[i]
            window.updatePosition(self.coord_list[i])

    def removeObj_fromList(self,Obj):
        self.pannedWindow_list.remove(Obj)
        self.coord_list.pop(-1)
        self.updateWindow()

if __name__ == '__main__':

    print("This script is panned window manager to control SpotWindow or ColocalWindow.")