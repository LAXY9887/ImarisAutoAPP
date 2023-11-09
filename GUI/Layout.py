# This is the main script of GUI

#%%
import tkinter as tk
from GUI_Coordination import Point
from SpotWindowUI import CreateSpotWindow
from MainFrame import CreateMainFrame
from Pages import *

if __name__ == '__main__':

    """ Layout """

    ## Create main frame
    mainWindow = CreateMainFrame(title = 'Demo of main window')

    ## Main Page window
    Pages = create_Pages(mainWindow)
 
    ## Panned Window Manager (Create Spot window)
    SpotPW_manager = CreateSpotWindow(parentPage = Pages["Create spots"])

    """ Developing """
    """ -------------------------------------------------------------------------------------------- """
    ## Run button 
    runBtn = tk.Button(mainWindow,text='RUN',bg='aquamarine')
    runBtn.place(anchor=tk.NW,x=10,y=580,width=200,height=60)

    ## Configure button 
    cfgBtn = tk.Button(mainWindow,text='Configure',bg='lightsteelblue')
    cfgBtn.place(anchor=tk.NW,x=240,y=580,width=80,height=60)

    ## Real time message 
    messagePanedWindow = tk.PanedWindow(mainWindow,bg="tomato",width=330,height=50)
    messagePanedWindow.place(anchor=tk.NW,x=10,y=520)
    """ -------------------------------------------------------------------------------------------- """

    ## Main loop
    mainWindow.mainloop()
# %%
