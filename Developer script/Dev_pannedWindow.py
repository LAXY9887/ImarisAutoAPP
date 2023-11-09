from GUI_Coordination import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import *

# Coord
Initial_coord = Point(0,0)
offset = Point(0,50)
coord_list = []
coord_list.append(Initial_coord)

# Test Label generation
window_list = []

class myPanWindow:

    def __init__(self,x,y) -> None:
        self.coord = Point(x,y)
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
        window_list.remove(self)
        coord_list.pop(-1)
        updateWindow()

    def getPanWindow(self):
        return self.spotWindow

    def updatePosition(self,NewPoint):
        self.spotWindow.place(anchor=tk.NW,x=NewPoint.x,y=NewPoint.y)

def PlaceWindow():

    # Calculate new point
    lp = coord_list[len(coord_list)-1]

    # Generate new label
    newOne = myPanWindow(lp.x,lp.y)
    window_list.append(newOne)

    # offset
    lp = Point(lp.x+offset.x,lp.y+offset.y)
    if lp not in coord_list:
        coord_list.append(lp)

def updateWindow():
    for i in range(len(coord_list)-1):
        window = window_list[i]
        window.updatePosition(coord_list[i])

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

btn = tk.Button(master=mainWindow,text="Add ONE",command=PlaceWindow)
btn.pack(side="bottom")

mainWindow.mainloop()