from pynput.mouse import Listener, Button
import pyautogui as PYG
import HandleStr as strManager
import Coordination as CorManager
from Spots import Spots
from Coordination import Point
import Actions
ActionManager = Actions.handleTarget()

class Colocalize:

    def __init__(self,name,savingDIR,total_ch,secondary_colocalize=None,secondary_col_savingDIR=None) -> None:

        ## Primary colocalize
        self._targetA_point = Point()
        self._targetB_point = Point()
        self._rel_targetA_point = Point(0,0)
        self._rel_targetB_point = Point(0,0)
        self._new_targetA_point = Point()
        self._new_targetB_point = Point()
        self._target_colocalize = Point()
        self.name = name
        self.savingDIR = savingDIR
        self.total_ch = total_ch
        self._isColocalize = False
        self._isFirst_Processed = False

        ## Secondary colocalize
        self._SeCtargetA_point = Point()
        self._SeCtargetB_point = Point()
        self._SeCrel_targetA_point = Point(0,0)
        self._SeCrel_targetB_point = Point(0,0)
        self._SeCnew_targetA_point = Point()
        self._SeCnew_targetB_point = Point()
        self._SeCtarget_colocalize = Point()
        self.secondary_colocalize = secondary_colocalize
        self.SecSavingDIR = secondary_col_savingDIR
        self._isSecColocalize = False
        self.secondary_spot = None
        self._isSceond_Processed = False

        # Create spot
        self.Create_Colocalize()

    def record_targetA_POS(self):
        print("Please select colocalize targetA.")
        with Listener(on_click=self.on_clickA) as listenser:
            listenser.join()

    def on_clickA(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._targetA_point.x = x
            self._targetA_point.y = y
            return False
    
    def record_targetB_POS(self):
        print("Please select colocalize targetB.")
        with Listener(on_click=self.on_clickB) as listenser:
            listenser.join()

    def on_clickB(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._targetB_point.x = x
            self._targetB_point.y = y
            return False

    def select_TargetAB(self):
        PYG.moveTo(self._new_targetA_point.x,self._new_targetA_point.y,duration=0.1)
        PYG.click(clicks=1, button=strManager.LEFT,duration=0.1)
        PYG.keyDown(strManager.CTRL)
        PYG.moveTo(self._new_targetB_point.x,self._new_targetB_point.y,duration=0.1)
        PYG.click(clicks=1, button=strManager.LEFT,duration=0.1)
        PYG.keyUp(strManager.CTRL)

    def record_SeCtargetA_POS(self):
        print("Please select colocalize targetA.")
        with Listener(on_click=self.on_SeCclickA) as listenser:
            listenser.join()

    def on_SeCclickA(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._SeCtargetA_point.x = x
            self._SeCtargetA_point.y = y
            return False
    
    def record_SeCtargetB_POS(self):
        print("Please select colocalize targetB.")
        with Listener(on_click=self.on_SeCclickB) as listenser:
            listenser.join()

    def on_SeCclickB(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._SeCtargetB_point.x = x
            self._SeCtargetB_point.y = y
            return False

    def select_SeCTargetAB(self):
        PYG.moveTo(self._SeCnew_targetA_point.x,self._SeCnew_targetA_point.y,duration=0.1)
        PYG.click(clicks=1, button=strManager.LEFT,duration=0.1)
        PYG.keyDown(strManager.CTRL)
        PYG.moveTo(self._SeCnew_targetB_point.x,self._SeCnew_targetB_point.y,duration=0.1)
        PYG.click(clicks=1, button=strManager.LEFT,duration=0.1)
        PYG.keyUp(strManager.CTRL)

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

    def record_SeCtarget_colocalize_POS(self):
        print("Please select colocalize to split spot.")
        with Listener(on_click=self.on_click_record_SeCtarget_colocalize) as listenser:
            listenser.join()

    def on_click_record_SeCtarget_colocalize(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._SeCtarget_colocalize.setPoint(x,y)
            return False

    def click_SeCtarget_colocalize_POS(self):
        PYG.moveTo(self._SeCtarget_colocalize.x,self._SeCtarget_colocalize.y)
        PYG.click(clicks=1, button=strManager.LEFT)

    def Enter_colocalize_name(self,point,offset,appendStr=""):
        PYG.moveTo(point.x+offset.x,point.y+offset.y)
        PYG.click(clicks=1, button=strManager.LEFT)
        PYG.click(clicks=2, button=strManager.LEFT)
        PYG.hotkey(strManager.CTRL, strManager.A)
        PYG.press(strManager.BACKSPACE)
        PYG.write(self.name+appendStr)
        PYG.press(strManager.ENTER)

    """ This section split spot into surface"""
    def Split_Spot(self):

        """ Close opened folder """
        if not self._isFirst_Processed:
            ## Click off opened folder
            ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)
            PYG.click(clicks=2)
        else:
            ## Click off opened folder (longer)
            ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN_LONG)
            PYG.click(clicks=2)

        if not self._isFirst_Processed:
            if not self._target_colocalize.isSet():
                self.record_target_colocalize_POS()
            else:
                self.click_target_colocalize_POS()
        else:
            if not self._SeCtarget_colocalize.isSet():
                self.record_SeCtarget_colocalize_POS()
            else:
                self.click_SeCtarget_colocalize_POS()
        
        # Hong+Elaine
        # 愛你

        """ This section Enter colocalize name """
        ## Click off Chinese typer
        if Actions.isChinese(): Actions.HandleChinese()

        """ Rename selected colocalize event """
        if not self._isFirst_Processed:
            self.Enter_colocalize_name(
                point= self._target_colocalize, 
                offset= CorManager.ENTER_colocalize_offset
            )
        else:
            self.Enter_colocalize_name(
                point= self._SeCtarget_colocalize, 
                offset= CorManager.ENTER_colocalize_offset,
                appendStr = "_" + self.secondary_colocalize
            )

        ## Click split spot to surface 1 
        ActionManager.click_target(target=strManager.MENU_BTN)

        ## Click split spot to surface 2
        ActionManager.click_target(target=strManager.SPOT_FUNC_BTN)

        ## Click split spot to surface 3 
        ActionManager.click_target(target=strManager.SPLT_SPOT_TO_SURFACE)

        ## Detect badSubScript
        BADsubscript = ActionManager.Find_target(target=strManager.BAD_SUBSCRIPT,interval = 0.2,timeOut = 3)
        if BADsubscript.isSet():
            ActionManager.click_target(target=strManager.SPLIT_SPOT_CLOSE,offset=CorManager.CLOSE_BADsubscript_offset)
            # Clear string: inside surface!
            ActionManager.click_Enter(target=strManager.INSIDE_SURFACE,string="BADsubscript",click=2)
            return self
        
        ## Wait off matlab window
        ActionManager.WaitOff_target(target=strManager.MATLAB_WINDOW)

        if not self._isFirst_Processed:
            ## Click off opened folder
            Close_folder_btn = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN_LONG,interval = 0.1,timeOut = 0.3)
            while not Close_folder_btn.isSet():
                Scroll_bar = ActionManager.Find_target(target=strManager.SCROLL_BAR)
                PYG.click(x=Scroll_bar.x,y=Scroll_bar.y,button=strManager.LEFT,clicks=1)
                Close_folder_btn = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN_LONG,interval = 0.1,timeOut = 0.3)
                if Close_folder_btn.isSet():
                    ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN_LONG,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)
                    break
            else:
                ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN_LONG,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)
        else:
            ## Find scroll bar & Close folder btn
            Close_folder_long_btn = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN_EX_LONG,interval = 0.1,timeOut = 0.3)
            while not Close_folder_long_btn.isSet():
                Scroll_bar = ActionManager.Find_target(target=strManager.SCROLL_BAR)
                PYG.click(x=Scroll_bar.x,y=Scroll_bar.y,button=strManager.LEFT,clicks=1)
                Close_folder_long_btn = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN_EX_LONG,interval = 0.1,timeOut = 0.3)
                ## Click off 2nd opened folder
                if Close_folder_long_btn.isSet():
                    ActionManager.click_target(target=strManager.CLOSE_FOLDER_BTN_EX_LONG,offset=CorManager.CLICK_OFF_FOLDER_BTN_EX_offset)
                    break
            else:
                ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN_EX_LONG,offset=CorManager.CLICK_OFF_FOLDER_BTN_EX_offset)

        ## Rename colocalize folder
        inside_surface = ActionManager.Find_target(target=strManager.INSIDE_SURFACE,interval = 0.1,timeOut = 0.3)
        while not inside_surface.isSet():
            Scroll_bar = ActionManager.Find_target(target=strManager.SCROLL_BAR)
            PYG.click(x=Scroll_bar.x,y=Scroll_bar.y,button=strManager.LEFT,clicks=1)
            inside_surface = ActionManager.Find_target(target=strManager.INSIDE_SURFACE,interval = 0.1,timeOut = 0.3)
            if inside_surface.isSet(): break

        if not self._isFirst_Processed:
            self.Enter_colocalize_name(
                point = inside_surface,
                offset= Point(0,0)
            )
        else:
            self.Enter_colocalize_name(
                point = inside_surface,
                offset= Point(0,0),
                appendStr = "_" + self.secondary_colocalize
            )

        ## Click statistic button
        ActionManager.click_target(target=strManager.STATISTIC_BTN)

        ## Click Overall button
        ActionManager.click_target(target=strManager.OVERALL_BTN,offset=CorManager.Overall_btn_offset)

        ## Click Export
        ActionManager.click_target(target=strManager.EXPORT_BTN, offset=CorManager.Export_excel_btn)

        ## Enter Export path
        if not self._isFirst_Processed:
            ActionManager.click_Enter(target=strManager.SAVING_DIR,string=self.savingDIR,offset=CorManager.Enter_export_path)
        else:
            ActionManager.click_Enter(target=strManager.SAVING_DIR,string=self.SecSavingDIR,offset=CorManager.Enter_export_path)

        ## Click SAVE
        ActionManager.click_target(target=strManager.SAVE_BTN)

        """ This section handle overwrite excel file"""
        Overwrite_Check = ActionManager.Find_target(target=strManager.EXIST_EXCEL_SIGN,timeOut = 2)
        if Overwrite_Check.isSet():
            ActionManager.click_target(target=strManager.EXIST_EXCEL_YES_BTN)

        if not self._isFirst_Processed: self._isFirst_Processed = True

        """ This section handle secondary colocalize"""
        if self.secondary_colocalize is not None and self._isColocalize and not self._isSceond_Processed:
            
            self._isSceond_Processed = True

            ## Click off opened folder
            FOLDER_BTN_long = ActionManager.Find_target(target=strManager.CLOSE_FOLDER_BTN_LONG,timeOut = 0.5)
            if FOLDER_BTN_long.isSet():
                ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN_LONG,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)

            ## Click Focus opened folder
            ActionManager.click_target(target=strManager.CLOSE_FOLDER_BTN,offset=CorManager.CLICK_OFF_FOLDER_BTN_shift)

            ## Create secondary spot
            if self.secondary_spot is None:
                self.secondary_spot = Spots(self.secondary_colocalize,total_channel=self.total_ch)
            else:
                self.secondary_spot.Create_spot()

            ## Colocalize secondary spot
            self.Create_Colocalize()

        """ Scroll to top """
        Scroll_bar_top = ActionManager.Find_target(target=strManager.SCROLL_BAR_TOP,timeOut = 2)
        if Scroll_bar_top.isSet():
            ActionManager.click_target(target=strManager.SCROLL_BAR_TOP,click=50)

        """ Close opened folder """
        if self._isSceond_Processed:
            ## Click off opened folder
            ActionManager.click_off_target(target=strManager.CLOSE_FOLDER_BTN,offset=CorManager.CLICK_OFF_FOLDER_BTN_offset)

        if self._isFirst_Processed: self._isFirst_Processed = False
        if self._isSceond_Processed: self._isSceond_Processed = False

    """ This section create colocalize """
    def Create_Colocalize(self):
        
        """ *** """
        if not self._isFirst_Processed:
            ## Focus on main folder
            ActionManager.click_target(target=strManager.HIERARCHY_ICON2,duration=0.15,offset=Point(0,-5))

        ## Click colocalize-1 
        ActionManager.click_target(target=strManager.MENU_BTN,duration=0.15)
        
        ## Click colocalize-2
        ActionManager.click_target(target=strManager.SPOT_FUNC_BTN)

        ## Click colocalize-3
        ActionManager.click_target(target=strManager.COLOCALIZE_BTN,duration=0.2)

        ## Wait colocalize window
        colocalize_string = ActionManager.Find_target(target=strManager.COLOCALIZE_WINDOW_STRING)
        
        # Create 1st colocalize
        if self._isFirst_Processed:
            if not self._targetA_point.isSet() and not self._targetB_point.isSet():
                self.record_targetA_POS()
                self._rel_targetA_point.setPoint(
                    newX = self._targetA_point.x - colocalize_string.x,
                    newY = self._targetA_point.y - colocalize_string.y
                )
                self._new_targetA_point.setPoint(
                    newX = colocalize_string.x + self._rel_targetA_point.x,
                    newY = colocalize_string.y + self._rel_targetA_point.y
                )
                self.record_targetB_POS()
                self._rel_targetB_point.setPoint(
                    newX = self._targetB_point.x - colocalize_string.x,
                    newY = self._targetB_point.y - colocalize_string.y
                )
                self._new_targetB_point.setPoint(
                    newX = colocalize_string.x + self._rel_targetB_point.x,
                    newY = colocalize_string.y + self._rel_targetB_point.y
                )
            else:
                self.select_TargetAB()
        else:
        # Create 2nd colocalize
            if not self._SeCtargetA_point.isSet() and not self._SeCtargetB_point.isSet():
                self.record_SeCtargetA_POS()
                self._SeCrel_targetA_point.setPoint(
                    newX = self._SeCtargetA_point.x - colocalize_string.x,
                    newY = self._SeCtargetA_point.y - colocalize_string.y
                )
                self._SeCnew_targetA_point.setPoint(
                    newX = colocalize_string.x + self._SeCrel_targetA_point.x,
                    newY = colocalize_string.y + self._SeCrel_targetA_point.y
                )
                self.record_SeCtargetB_POS()
                self._SeCrel_targetB_point.setPoint(
                    newX = self._SeCtargetB_point.x - colocalize_string.x,
                    newY = self._SeCtargetB_point.y - colocalize_string.y
                )
                self._SeCnew_targetB_point.setPoint(
                    newX = colocalize_string.x + self._SeCrel_targetB_point.x,
                    newY = colocalize_string.y + self._SeCrel_targetB_point.y
                )
            else:
                self.select_SeCTargetAB()

        """ This section click ok on colocalize window"""
        ActionManager.click_target(target=strManager.COLOCALIZE_WINDOW)

        """ This section wait out colocalize window """
        ActionManager.Find_target(target=strManager.COLOCALIZE_RATIO_OK_BTN)

        """ This section Enter 0.5 on text box """
        PYG.press(strManager.BACKSPACE)
        if Actions.isChinese(): Actions.HandleChinese()
        PYG.write(strManager.COLOCALIZE_RATIO)
        ActionManager.click_target(target = strManager.COLOCALIZE_RATIO_OK_BTN, offset=CorManager.COLOCALIZE_ratio_offset)

        """ This section determine if there is any colocalize """
        Colocalize_Check = ActionManager.Find_target(target=strManager.NO_COLOCALIZE_WINDOW,timeOut = 3,conf=0.95)

        if Colocalize_Check.isSet():
            self._isColocalize = False
            ActionManager.click_target(target=strManager.NO_COLOCALIZE_WINDOW,offset=CorManager.NO_COLOCALIZE_window_offset)
            ActionManager.click_target(target=strManager.CREATE_FOLDER_BTN,offset=Point(3,0))
        else:
            self._isColocalize = True
            self.Split_Spot()
        
        """ This section wait off co-localize matlab window """
        ActionManager.WaitOff_target(target=strManager.MATLAB_WINDOW)

        return self

    def Print_Info(self):
        print("Colocalize name:{} spotA: {}".format(self.name,self._targetA_point))
        print("Colocalize name:{} spotB: {}".format(self.name,self._targetB_point))
        print("Colocalize name:{} NEWspotA:{}".format(self.name,self._new_targetA_point))
        print("Colocalize name:{} NEWspotB:{}".format(self.name,self._new_targetB_point))
        print("Colocalize name:{} Select_colocalize:{}".format(self.name,self._target_colocalize))
        print("Colocalize name:{} Relative_A_spot:{}".format(self.name,self._rel_targetA_point))
        print("Colocalize name:{} Relative_B_spot:{}".format(self.name,self._rel_targetB_point))
        print("Colocalize name:{} Save to :{}".format(self.name,self.savingDIR))

if __name__ == "__main__":
    print("Colocalize Object")