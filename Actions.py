import HandleStr as strManager
import pyautogui as PYG
import time
import subprocess
import Coordination as CorManager
from Coordination import Point

class handleTarget:

    def __init__(self) -> None:
        pass

    def click_target(self,target:str,interval = 0.1,timeOut = 120,offset=Point(0,0),click=1,button=strManager.LEFT,duration=0,conf=-1):
        if conf == -1:
            target_loc = self.Find_target(target,interval = interval,timeOut = timeOut, conf=0.95)
        else:
            target_loc = self.Find_target(target,interval = interval,timeOut = timeOut, conf=conf)
        if target_loc.isSet():
            PYG.click(
                x = target_loc.x + offset.x, y = target_loc.y + offset.y,
                clicks=click, button=button,duration=duration
            )
        else:
            print("Target not found")

    def click_off_target(self,target:str,interval = 0.1,timeOut = 120,offset=Point(0,0),click=1,button=strManager.LEFT,duration=0):
        target_loc = self.Find_target(target,interval = interval,timeOut = timeOut)
        find_next = target_loc.isSet()
        while find_next:
            find_next_loc = self.Find_target(target,interval = 0.1 ,timeOut = 0.3)
            find_next = find_next_loc.isSet()
            if find_next:
                PYG.click(
                x = find_next_loc.x + offset.x, y = find_next_loc.y + offset.y,
                clicks=click, button=button,duration=duration)

    def click_Enter(self,target:str,string:str,interval = 0.1,timeOut = 120,offset=Point(0,0),click=1,button=strManager.LEFT,duration=0):
        target_loc = self.Find_target(target,interval = interval,timeOut = timeOut, conf=0.95)
        if target_loc.isSet():
            PYG.click(
                x = target_loc.x + offset.x, y = target_loc.y + offset.y,
                clicks=click, button=button,duration=duration
            )
            PYG.hotkey(strManager.CTRL,strManager.A,strManager.BACKSPACE)
            PYG.write(string)
            PYG.press(strManager.ENTER)
        else:
            print("Target not found")

    def scroll_target(self,target:str,steps:int,interval = 0.1,timeOut = 120,offset=Point(0,0)):
        target_loc = self.Find_target(target,interval = interval,timeOut = timeOut, conf=0.95)
        if target_loc.isSet:
            PYG.moveTo(x=target_loc.x+offset.x, y=target_loc.y+offset.y,duration=0.2)
            for i in range(steps): PYG.scroll(-i)
        else:
            print("Target not found")

    def Find_target(self, target,interval = 0.1,timeOut = 120, conf=-1):
        timer = 0
        Finished = False
        while not Finished:
            find_target = strManager.getAsset(target)
            if conf > 0:
                target_loc = PYG.locateCenterOnScreen(find_target,confidence=conf)
            else:
                target_loc = PYG.locateCenterOnScreen(find_target)
            if target_loc is None:
                time.sleep(interval)
                timer += interval
                if timer >= timeOut:
                    timer = 0
                    Finished = True
                    return Point(-1,-1)
            else:
                Finished = True
                return Point(target_loc.x,target_loc.y)

    def WaitOff_target(self, target,interval = 0.1,timeOut = 120):
        timer = 0
        Finished = False
        while not Finished:
            find_target = strManager.getAsset(target)
            target_loc = PYG.locateCenterOnScreen(find_target)
            if target_loc is not None:
                self.target_exist = True
                time.sleep(interval)
                timer += interval
                if timer >= timeOut:
                    timer = 0
                    Finished = True
            else:
                Finished = True

ActionManager = handleTarget()

""" This section detect type mode """
def HandleChinese():
    ActionManager.click_target(target=strManager.TYPE_MODE_ICON,conf=0.8)
    PYG.move(0,-500)

""" This section click off type mode """
def isChinese():
    Type_Mode = ActionManager.Find_target(strManager.TYPE_MODE_ICON,timeOut=0.3,conf=0.8)
    return Type_Mode.isSet()

def Initial_Imaris(fileDIR):
    """ 00. This section call Imaris and open *.ims files. """
    subprocess.Popen([strManager.IMARIS_DIR,fileDIR])

    """ 01. This section wait for initial error and click it off. """
    ActionManager.click_target(
        target=strManager.ERROR_ICON,
        interval=0.2, timeOut=120,
        offset=CorManager.Initial_ERROR_offset
    )

    ## Click off Chinese typer
    if isChinese(): HandleChinese()

""" This function export IMS file"""
def Export_IMS(Export_path):

    ## Click Export IMS-1 
    ActionManager.click_target(target=strManager.EXPORT_IMS_BTN)

    """ This section Enter colocalize name """
    ## Click off Chinese typer
    if isChinese(): HandleChinese()

    ## Enter saving directory
    ActionManager.click_Enter(target=strManager.EXPORT_IMS_WINDOW,string=Export_path,offset=CorManager.Export_IMS_window_offset)

    ## Click off overwriting window This is bad!
    OVERWRITE_ims = ActionManager.Find_target(target=strManager.OVERWRITE_IMS,timeOut=3)
    if OVERWRITE_ims.isSet():
        ActionManager.click_target(target=strManager.OVERWRITE_IMS_YES_BTN)

    ## Wait out progress bar 
    ActionManager.Find_target(target=strManager.PROGRESS_BAR,interval=0.5, timeOut=10,conf=0.95)

    ## Wait off progress bar cancel button
    ActionManager.WaitOff_target(target=strManager.PROGRESS_BAR_CANCEL_BTN,interval=0.3)

    ## Click Close Imaris
    ActionManager.click_target(target=strManager.CLOSE_IMARIS_BTN,offset=CorManager.CLose_imaris_btn_offset)

    ## Wait off Imaris icon
    ActionManager.WaitOff_target(target=strManager.IMARIS_ICON,interval=0.3)

if __name__ == "__main__":
    print("Action Functions and Objects")
