#%%
## Setting Section

title = "Main Frame"
icon = "icon.ico"
window_size='350x650'
windowLock = True

#%%
## Coding Section 
import tkinter as tk

def CreateMainFrame(title,window_size=window_size,windowLock = windowLock,icon = icon):

    """ False: DO not lock window at front. True: window is always at front. """
    mainWindow = tk.Tk()
    mainWindow.title(title)
    mainWindow.geometry(window_size)
    mainWindow.resizable(False, False)
    #mainWindow.iconbitmap('icon.ico')

    """ This lock GUI window at the front. """
    windowLock = windowLock
    mainWindow.wm_attributes('-topmost',windowLock)

    return mainWindow

if __name__ == '__main__':

    print("Main Frame Demo")
    mainWindow = CreateMainFrame("Demo")
    mainWindow.mainloop()