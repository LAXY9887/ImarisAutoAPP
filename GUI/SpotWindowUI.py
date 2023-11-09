#%%
## Setting Section
from GUI_Coordination import Point
import HandleStringUI as StrUI

# Create Spot Window
SpotWindowHeight = 150
SpotWindowColor = "oldlace"
Initial_coord = Point(5,5)
SpotWindowOffset = Point(0,155)

# Create Add one button
ADDbutton_width = 45
ADDbutton_height = 2
ADDbutton_x = 2
ADDbutton_y = 435
ADDbutton_Text = StrUI.ADDONE

#%%
## Coding Section 

import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import HandleStringUI as strManager
from Pages import create_Pages
from MainFrame import CreateMainFrame
from PannedWindowManager import PannedWindowManager

class SpotWindow:

    def __init__(
        self, coord, parentPage, manager,
        windowHeight = SpotWindowHeight,
        windowColor = SpotWindowColor
    ) -> None:
        
        ## Window parameters
        self.coord = coord
        self.parentPage = parentPage
        self.master = parentPage.getFrame()
        self.manager = manager
        self.width = parentPage.width * 0.9
        self.height = windowHeight
        self.bg_color = windowColor

        ## 
        self._SpotID = ""
        self.show_CreateSpotWindow()
        self.PanWindow = self.getSpotWindow()

    def show_CreateSpotWindow(self):

        ## Spot window
        self.spotWindow = tk.PanedWindow(master=self.master,bg=self.bg_color,width=self.width,height=self.height)
        self.spotWindow.place(anchor=tk.NW,x=self.coord.x,y=self.coord.y)

        ## Spot icon image
        spotIcon_x, spotIcon_y = 5, 5
        spotIcon_width, spotIcon_height = 50, 50
        spotIcon_img = Image.open(strManager.getAssetUI(strManager.SPOT_ICON_1))
        spotIcon_img = spotIcon_img.resize((spotIcon_width,spotIcon_height),Image.Resampling.LANCZOS)
        spotIcon_photo = ImageTk.PhotoImage(spotIcon_img)
        spotIcon = tk.Label(master=self.spotWindow, image=spotIcon_photo)
        spotIcon.image = spotIcon_photo
        spotIcon.place(anchor=tk.NW,x=spotIcon_x,y=spotIcon_y,width=spotIcon_width,height=spotIcon_height)

        ## Spot ID label
        spotID_label_x, spotID_label_y = 55, 5
        spotID_label_fontSize = 14
        spotID_label = tk.Label(
            master=self.spotWindow,
            text=strManager.SPOT_ID_LABEL,
            font=(strManager.ARIAL, spotID_label_fontSize),bg=self.bg_color
        )
        spotID_label.place(anchor=tk.NW,x=spotID_label_x, y=spotID_label_y)

        ## Text BOX for Spot ID input
        spotID_TextBOX_x, spotID_TextBOX_y = 130, 5
        spotID_TextBOX_w = 12
        self.spotID_TextBOX = tk.Entry(
            master=self.spotWindow,
            font= (strManager.ARIAL, spotID_label_fontSize),
            width = spotID_TextBOX_w, state = tk.NORMAL
        )
        self.spotID_TextBOX.place(anchor=tk.NW, x = spotID_TextBOX_x, y = spotID_TextBOX_y)

        ## Delete spot button
        self.delete_btn = tk.Button(master=self.spotWindow, width=1,height=1,text="X",command=self.destory_SpotWindow)
        self.delete_btn.place(anchor=tk.NW,x=275,y=5)

    def getSpotWindow(self):
        return self.spotWindow

    def getSpotID(self):
        self._SpotID = self.spotID_TextBOX.get()
        return self._SpotID

    def PrintInfo(self):
        print("SpotID = ",self._SpotID)

    def destory_SpotWindow(self):
        self.spotWindow.destroy()
        self.manager.removeObj_fromList(self)

    def updatePosition(self,NewPoint):
        self.spotWindow.place(anchor=tk.NW,x=NewPoint.x,y=NewPoint.y)

# Create Panned Window Manager and panned window
def CreateSpotWindow(parentPage):

    ## Create a manager
    manager = PannedWindowManager(
        Initial_coord,SpotWindowOffset,SpotWindow,parentPage
    )

    ## Create button 
    button_width = ADDbutton_width
    button_height = ADDbutton_height
    button_x = ADDbutton_x
    button_y = ADDbutton_y
    createSpot_btn = tk.Button(
        master=parentPage.getPanedWindow(),width=button_width,height=button_height,
        text=ADDbutton_Text,command=manager.PlaceWindow
    )
    createSpot_btn.place(anchor=tk.NW,x=button_x,y=button_y)

    return manager

if __name__ == '__main__':
    
    print("This script create pages panned window.")

    ## Create main frame
    mainWindow = CreateMainFrame(title = 'Demo of create spot window')
    
    ## Create pages window
    Pages = create_Pages(mainWindow)

    # Panned Window Manager
    SpotPW_manager = CreateSpotWindow(parentPage = Pages["Create spots"])

    ## UI LOOP
    mainWindow.mainloop()

# %%
