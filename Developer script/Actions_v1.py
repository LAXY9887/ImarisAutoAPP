import subprocess
import Coordination as CorManager
import HandleStr as strManager
import pyautogui as PYG
from ObjChecker import ObjChecker
import time

""" Action Checker """
Checker = ObjChecker(wait_sec=0.1,timeout=120)

""" This section detect type mode """
def HandleChinese():
    Click_Type_Mode = Click_Target(target=strManager.TYPE_MODE_ICON)
    Checker.wait_Action(Click_Type_Mode.Click_Function())
    timer_ring = Checker.checkTime()
    if timer_ring: return False
    return True

""" This section click off type mode """
def isChinese():
    Type_Mode = strManager.getAsset(strManager.TYPE_MODE_ICON)
    Type_Mode_loc = PYG.locateCenterOnScreen(Type_Mode)
    if Type_Mode_loc != None:
        return True
    else:
        return False

""" This section keep processing """
def Process_Checker(checker):
    if checker is False: 
        return False
    else:
        return True

def Create_new_spotFolder():
    ## Click Create folder
    Click_Create_Folder = Click_Target(target=strManager.CREATE_FOLDER_BTN,offsetX=20)
    Checker.wait_Action(Click_Create_Folder.Click_Function())

    if isChinese():HandleChinese()

    ## Click change folder name
    Click_Rename_Folder = Click_Target(target=strManager.NEW_FOLDER,str=strManager.SPOT_FOLDER_NAME,click=2)
    Checker.wait_Action(Click_Rename_Folder.Click_Enter_Function())
    PYG.moveRel(xOffset=0,yOffset=50)
    PYG.click(button=strManager.LEFT,clicks=2)

def Initial_Imaris(fileDIR):
    """ 00. This section call Imaris and open *.ims files. """
    subprocess.Popen([strManager.IMARIS_DIR,fileDIR])

    """ 01. This section wait for initial error and click it off. """
    find_Initial_ERROR = Click_Target(
        target=strManager.ERROR_ICON,
        offsetX=CorManager.Initial_ERROR_offsetX,
        offsetY=CorManager.Initial_ERROR_offsetY
        )
    Checker.wait_Action(find_Initial_ERROR.Click_Function())
    #Create_new_spotFolder()
    return True

""" This function export IMS file"""
def Export_IMS(Export_path):

    ## Click Export IMS-1 
    Click_EXPORT_btn =  Click_Target(target=strManager.EXPORT_IMS_BTN,duration=0.15)
    Checker.wait_Action(Click_EXPORT_btn.Click_Function())

    """ This section Enter colocalize name """
    ## Click off Chinese typer
    if isChinese(): HandleChinese()

    ## Enter saving directory
    ENTER_Exporting_dir = Click_Target(target=strManager.EXPORT_IMS_WINDOW,offsetX=-15,str=Export_path)
    Checker.wait_Action(ENTER_Exporting_dir.Click_Enter_Function())

    ## Click off overwriting window
    Click_Overwrite_IMS =  Click_Target(target=strManager.OVERWRITE_IMS,offsetX=415,offsetY=105)
    Little_timer = ObjChecker(wait_sec=0.1,timeout=3)
    Little_timer.wait_Action(Click_Overwrite_IMS.Click_Function())

    ## Wait out progress bar 
    Wait_Progress_bar = Wait_Target(target=strManager.PROGRESS_BAR,disappear=False)
    Checker.wait_Action(Wait_Progress_bar.Wait_Function())

    ## Wait off progress bar cancel button
    Wait_Progress_Cancel_btn = Wait_Target(target=strManager.PROGRESS_BAR_CANCEL_BTN,disappear=True)
    Checker.wait_Action(Wait_Progress_Cancel_btn.Wait_Function())

    ## Click Close Imaris
    Click_CloseIMS_btn =  Click_Target(target=strManager.CLOSE_IMARIS_BTN,duration=0.1, offsetX = 50)
    Checker.wait_Action(Click_CloseIMS_btn.Click_Function())

    ## Wait off Imaris icon
    Wait_IMARIS_icon = Wait_Target(target=strManager.IMARIS_ICON,disappear=True)
    Checker.wait_Action(Wait_IMARIS_icon.Wait_Function())

    return True

""" This section click something. """
class Click_Target:
    
    def __init__(self,target,click=1,button=strManager.LEFT,offsetX=0,offsetY=0,duration=0,str="") -> None:
        self.target = target
        self._targetPosX = -1
        self._targetPosY = -1
        self.click = click
        self.button = button
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.duration = duration
        self.str = str

    def click_Target(self):
        click_target = strManager.getAsset(self.target)
        click_target_loc = PYG.locateCenterOnScreen(click_target)
        if click_target_loc != None:
            PYG.moveTo(click_target_loc.x+self.offsetX, click_target_loc.y+self.offsetY,duration=self.duration)
            PYG.click(clicks=self.click, button=self.button,duration=self.duration)
            return True
        return None
    
    def click_off_Target(self):
        click_target = strManager.getAsset(self.target)
        click_target_loc = PYG.locateCenterOnScreen(click_target)
        if click_target_loc != None:
            PYG.moveTo(click_target_loc.x+self.offsetX, click_target_loc.y+self.offsetY,duration=self.duration)
            PYG.click(clicks=self.click, button=self.button,duration=self.duration)
            click_target_loc = PYG.locateCenterOnScreen(click_target)
            if click_target_loc != None:
                return None
            else:
                return True
        return None
    
    def click_Enter(self):
        click_target = strManager.getAsset(self.target)
        click_target_loc = PYG.locateCenterOnScreen(click_target)
        if click_target_loc != None:
            PYG.moveTo(click_target_loc.x+self.offsetX, click_target_loc.y+self.offsetY,duration=self.duration)
            PYG.click(clicks=self.click, button=self.button,duration=self.duration)
            PYG.hotkey(strManager.CTRL,strManager.A,strManager.BACKSPACE)
            PYG.write(self.str)
            PYG.press(strManager.ENTER)
            return True
        return None

    def Click_Function(self):
        return self.click_Target
    
    def Click_Off_Function(self):
        return self.click_off_Target
    
    def Click_Enter_Function(self):
        return self.click_Enter

""" This section wait something. """
class Wait_Target:
    
    def __init__(self,target,disappear=False) -> None:
        self.target = target
        self.isExist = False
        self.disappear = disappear
        self.PosX = -1
        self.PosY = -1

    def wait_Target(self):
        wait_target = strManager.getAsset(self.target)
        wait_target_loc = PYG.locateCenterOnScreen(wait_target)
        if wait_target_loc != None:
            self.isExist = True
            self.PosX = wait_target_loc.x
            self.PosY = wait_target_loc.y
            if not self.disappear:
                return True
            else:
                return None
        else:
            self.isExist = False
            if not self.disappear:
                return None
            else:
                return True

    def Wait_Function(self):
        return self.wait_Target    

""" This section drag something. """
class Drag_Target:
    
    def __init__(self,target_X,target_Y,to_X,to_Y,button=strManager.LEFT,duration=0) -> None:
        self.target_X = target_X
        self.target_Y = target_Y
        self.to_X = to_X
        self.to_Y = to_Y
        self.button = button
        self.duration = duration

    def Drag_Target(self):
        PYG.moveTo(self.target_X, self.target_Y,duration=self.duration)
        # PYG.dragTo(self.to_X,self.to_Y,button=self.button,duration=self.duration)
        PYG.mouseDown(button=strManager.LEFT)
        PYG.moveTo(self.to_X,self.to_Y,duration=self.duration)
        PYG.mouseUp(button=strManager.LEFT,duration=self.duration)
        return True

    def Drag_Function(self):
        return self.Drag_Target

""" This section scroll on scroll bar """
class Scroll_Target:

    def __init__(self,steps,target_X,target_Y,offsetX=0,offsetY=0) -> None:
        self.steps = steps
        self.target_X = target_X
        self.target_Y = target_Y
        self.offsetX = offsetX
        self.offsetY = offsetY
    
    def Scrolling_Target(self):
        PYG.moveTo(x=self.target_X+self.offsetX, y=self.target_Y+self.offsetY)
        for i in range(self.steps): PYG.scroll(-i)
        return True
    
    def Scrolling_Function(self):
        return self.Scrolling_Target

if __name__ == "__main__":
    print("Action Functions and Objects")

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

    class handleTarget:

        def __init__(self,target) -> None:
            self.target = target
            self.Coord = Point()
            self.target_found = False

        def locate_target(self):
            find_target = strManager.getAsset(self.target)
            target_loc = PYG.locateCenterOnScreen(find_target)
            return target_loc

        def click_target(self,click=1,button=strManager.LEFT,duration=0):
            if self.target_found:
                PYG.click(
                    x = self.Coord.x, y = self.Coord.y,
                    clicks=click, button=button,duration=duration
                )
            else:
                print("Target not found")

        def Find_target(self,interval = 0.1,timeOut = 2.0):
            timer = 0
            Finished = False
            while not Finished:
                loc = self.locate_target()
                if loc is None:
                    time.sleep(interval)
                    timer += interval
                    if timer >= timeOut:
                        timer = 0
                        Finished = True
                        self.target_found = False
                else:
                    Finished = True
                    self.target_found = True
                    self.Coord.setPoint(loc.x,loc.y)

    ##
    Error_icon = strManager.ERROR_ICON
    Error_iconObj = handleTarget(Error_icon)
    Error_iconObj.Find_target(interval = 0.1,timeOut = 2.0)
    Error_iconObj.click_target()
    