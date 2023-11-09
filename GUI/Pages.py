#%%
## Setting Section

# PanedWindow settings
PanedWindow_width = 330
PanedWindow_height = 480
PanedWindow_x = 10
PanedWindow_y = 35
PanedBtn_width = 80
PanedBtn_height = 25

## Frame Settings
frame_w = PanedWindow_width - 4
frame_h = PanedWindow_height -50

# Pages window
Pages_dict = {
    "Music":{"bg_color":"pink","button_x":250,"button_y":10},
    "Colocalize":{"bg_color":"gold","button_x":90,"button_y":10},
    "Message Log":{"bg_color":"blue","button_x":170,"button_y":10},
    "Create spots":{"bg_color":"gray","button_x":10,"button_y":10}
}

#%%
## Coding Section 

import tkinter as tk
from MainFrame import CreateMainFrame

class myPanedWindow():

    def __init__(
        self,inherit,name,bg_color,button_x, button_y
        ,x=PanedWindow_x,y=PanedWindow_y,
        width=PanedWindow_width,height=PanedWindow_height,
        button_width = PanedBtn_width,button_height=PanedBtn_height,
        frameWidth = frame_w, frameHeight = frame_h
        ) -> None:
        self.inherit = inherit
        self.name = name
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.otherPages = []

        ## Frame Setting
        self.frame_w = frameWidth
        self.frame_h = frameHeight

        ## Generate panned window and its button
        self.create_PanedWindow()
        self.show_pageBtn()

    def create_PanedWindow(self) -> None:
        
        ## Panned Window
        self.PanedWindow = tk.PanedWindow(self.inherit,bg=self.bg_color,width=self.width,height=self.height)
        self.PanedWindow.place(anchor=tk.NW,x=self.x,y=self.y)

        ## Frame
        self.Frame = tk.Frame(self.PanedWindow,width=self.frame_w,height=self.frame_h,bg="white")
        self.Frame.place(anchor=tk.NW,x=1,y=2)

        ## Scroll bar
        self.scroll = tk.Scrollbar(self.Frame)
        self.scroll.place(anchor=tk.NW, x=frame_w-20, y=0,height=frame_h)

    def hide_PanedWindow(self) -> None:
        self.PanedWindow.place_forget()

    def show_PanedWindow(self) -> None:
        self.PanedWindow.place(anchor=tk.NW,x=self.x,y=self.y)
    
    def getPanedWindow(self):
        return self.PanedWindow

    def getFrame(self):
        return self.Frame

    def show_pageBtn(self) -> None:
        self.PageBtn = tk.Button(self.inherit,text=self.name,bg=self.bg_color,bd=0,command=self.switch_Pages)
        self.PageBtn.place(anchor=tk.NW,x=self.button_x,y=self.button_y,height=self.button_height,width=self.button_width)
    
    def getPageBtn(self):
        return self.PageBtn

    def switch_Pages(self):
        for each in self.otherPages:
            each.hide_PanedWindow()
        self.show_PanedWindow()


def create_Pages(inherit):
    PageObj_dict = {}
    for each in Pages_dict:
        pageObj = myPanedWindow(
            inherit = inherit,
            name = each,
            bg_color = Pages_dict[each]["bg_color"],
            button_x= Pages_dict[each]["button_x"],
            button_y= Pages_dict[each]["button_y"]
        )
        PageObj_dict[each] = pageObj

    ## Add other pages to each page
    for each in PageObj_dict:
        for item in PageObj_dict:
            if item != each:
                PageObj_dict[each].otherPages.append(PageObj_dict[item])
    
    return PageObj_dict


if __name__ == '__main__':
    
    print("This script create pages panned window.")

    ## Create main frame
    mainWindow = CreateMainFrame(title = 'Demo of panned window')
    
    ## Create Pages
    mainPages = create_Pages(inherit = mainWindow)
    
    ## UI LOOP
    mainWindow.mainloop()

# %%
