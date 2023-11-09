from GUI_Coordination import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import *

class PannedWindowManager:

    def __init__(self,Initial_coord,offset) -> None:
        self.Initial_coord = Initial_coord
        self.offset = offset
        self.coord_list = [self.Initial_coord]
        self.pannedWindow_list = []

    def PlaceWindow(self):

        # Calculate new point
        lp = self.coord_list[len(self.coord_list)-1]

        # Generate new label
        newOne = myPanWindow(lp.x,lp.y,manager=self)
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

class myPanWindow:

    def __init__(self,x,y,manager) -> None:
        self.coord = Point(x,y)
        self.manager = manager
        self.showPanWindow()
        self.PanWindow = self.getPanWindow()

    def showPanWindow(self):
        # Show panned Window
        self.spotWindow = tk.PanedWindow(master=mainWindow,bg="gold",width=150,height=30)
        self.spotWindow.place(anchor=tk.NW,x=self.coord.x,y=self.coord.y)
        self.label = tk.Label(master=self.spotWindow,text="TSET Label",bg="gray")
        self.label.place(anchor=tk.NW,x=30,y=0)
        self.btn = tk.Button(master=self.spotWindow,text="X",command=self.destoryPanWindow)
        self.btn.place(anchor=tk.NW,x=0,y=0)

    def destoryPanWindow(self):
        self.spotWindow.destroy()
        self.manager.removeObj_fromList(self)

    def getPanWindow(self):
        return self.spotWindow

    def updatePosition(self,NewPoint):
        self.spotWindow.place(anchor=tk.NW,x=NewPoint.x,y=NewPoint.y)

#%%
# Coord
Initial_coord = Point(0,0)
offset = Point(0,50)

# Manager
PW_manager = PannedWindowManager(Initial_coord,offset)

#%%
# GUI 
title = "Main Frame"
icon = "icon.ico"
window_size='600x600'
windowLock = True

mainWindow = tk.Tk()
mainWindow.title(title)
mainWindow.geometry(window_size)
mainWindow.resizable(False, False)

windowLock = windowLock
mainWindow.wm_attributes('-topmost',windowLock)

btn = tk.Button(master=mainWindow,text="Add ONE",command=PW_manager.PlaceWindow)
btn.pack(side="bottom")

mainWindow.mainloop()