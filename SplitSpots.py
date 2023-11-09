from pynput.mouse import Listener, Button
import pyautogui as PYG
import HandleStr as strManager
import Coordination as CorManager
from Coordination import Point
import Actions
ActionManager = Actions.handleTarget()

class SplitSpot:

    def __init__(self,name,savingDIR) -> None:
        self.name = name
        self.savingDIR = savingDIR
        self._target_colocalize = Point()
        self.Spliting()

    ## Click off opened folder
    def closeFolders(self,button,btn_offset=Point(0,0)):
        ActionManager.click_off_target(target=button,offset=btn_offset)
        PYG.click(clicks=2)

    def record_target_colocalize_POS(self):
        print("Please select colocalize to split spot.")
        with Listener(on_click=self.on_click_record_target_colocalize) as listenser:
            listenser.join()

    def on_click_record_target_colocalize(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._target_colocalize.setPoint(x,y)
            return False

    def click_target_colocalize_POS(self):
        PYG.moveTo(self._target_colocalize.x,self._target_colocalize.y)
        PYG.click(clicks=1, button=strManager.LEFT)

    def Enter_object_name(self,point,offset,appendStr=""):
        PYG.moveTo(point.x+offset.x,point.y+offset.y)
        PYG.click(clicks=1, button=strManager.LEFT)
        PYG.click(clicks=2, button=strManager.LEFT)
        PYG.hotkey(strManager.CTRL, strManager.A)
        PYG.press(strManager.BACKSPACE)
        PYG.write(self.name+appendStr)
        PYG.press(strManager.ENTER)

    """ This section split spot into surface"""
    def Spliting(self):

        if not self._target_colocalize.isSet():
            self.record_target_colocalize_POS()
        else:
            self.click_target_colocalize_POS()
        
        # Hong+Elaine
        # 愛你

        """ This section Enter colocalize name """
        ## Click off Chinese typer
        if Actions.isChinese(): Actions.HandleChinese()

        """ Rename selected colocalize event """
        self.Enter_object_name(
            point= self._target_colocalize, 
            offset= Point(0,0)
        )

        ## Click split spot to surface 1 
        ActionManager.click_target(target=strManager.MENU_BTN)

        ## Click split spot to surface 2
        ActionManager.click_target(target=strManager.SPOT_FUNC_BTN)

        ## Click split spot to surface 3 
        ActionManager.click_target(target=strManager.SPLT_SPOT_TO_SURFACE)

        ## Wait matlab window
        ActionManager.Find_target(target=strManager.MATLAB_WINDOW)

        ## Detect badSubScript
        BADsubscript = ActionManager.Find_target(target=strManager.BAD_SUBSCRIPT,interval = 0.2,timeOut = 3)
        if BADsubscript.isSet():
            ActionManager.click_target(target=strManager.SPLIT_SPOT_CLOSE,offset=CorManager.CLOSE_BADsubscript_offset)
            # Clear string: inside surface!
            ActionManager.click_Enter(target=strManager.INSIDE_SURFACE,string="BADsubscript",click=2)
            return self

        ## Wait off matlab window
        ActionManager.WaitOff_target(target=strManager.MATLAB_WINDOW)

        ## Click off opened folder
        Close_folder_btn = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN,interval = 0.1,timeOut = 0.3)
        while not Close_folder_btn.isSet():
            Scroll_bar = ActionManager.Find_target(target=strManager.SCROLL_BAR,timeOut = 0.3)
            PYG.click(x=Scroll_bar.x,y=Scroll_bar.y,button=strManager.LEFT,clicks=1)
            Close_folder_btn = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN,interval = 0.1,timeOut = 0.3)
            if Close_folder_btn.isSet():
                ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)
                break
        else:
            ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)

        ## Rename colocalize folder
        inside_surface = ActionManager.Find_target(target=strManager.INSIDE_SURFACE,interval = 0.1,timeOut = 0.3)
        while not inside_surface.isSet():
            Scroll_bar = ActionManager.Find_target(target=strManager.SCROLL_BAR,timeOut = 0.3)
            PYG.click(x=Scroll_bar.x,y=Scroll_bar.y,button=strManager.LEFT,clicks=1)
            inside_surface = ActionManager.Find_target(target=strManager.INSIDE_SURFACE,interval = 0.1,timeOut = 0.3)
            if inside_surface.isSet(): break

        self.Enter_object_name(
            point = inside_surface,
            offset= Point(0,0)
        )

        ## Click statistic button
        ActionManager.click_target(target=strManager.STATISTIC_BTN)

        ## Click Overall button
        ActionManager.click_target(target=strManager.OVERALL_BTN,offset=CorManager.Overall_btn_offset)

        ## Click Export
        ActionManager.click_target(target=strManager.EXPORT_BTN, offset=CorManager.Export_excel_btn)

        ## Enter Export path
        ActionManager.click_Enter(target=strManager.SAVING_DIR,string=self.savingDIR,offset=CorManager.Enter_export_path)

        ## Click SAVE
        ActionManager.click_target(target=strManager.SAVE_BTN,duration=0.5)

        """ This section handle overwrite excel file"""
        Overwrite_Check = ActionManager.Find_target(target=strManager.EXIST_EXCEL_SIGN,timeOut = 2)
        if Overwrite_Check.isSet():
            ActionManager.click_target(target=strManager.EXIST_EXCEL_YES_BTN)

        """ Scroll to top """
        Scroll_bar_top = ActionManager.Find_target(target=strManager.SCROLL_BAR_TOP,timeOut = 2)
        if Scroll_bar_top.isSet():
            ActionManager.click_target(target=strManager.SCROLL_BAR_TOP,click=50)

if __name__ == "__main__":
    print("Spliting spot to surface")