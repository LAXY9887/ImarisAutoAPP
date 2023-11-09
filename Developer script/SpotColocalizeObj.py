"""
03.1 Pop out GUI to hind (manually) click on new spot. 
 -- Include Spot Name (User Enter)
03.2 User (manually) click on new spot, recording mouse position.
03.3 User (manually) Enter spot name, recording spot name.
03.4 User (manually) selet drop list, recording drop list position.
03.5 User (manually) selet spot program, recording spot program position. 
03.6 User (manually) click on Start Process button, recording Start Process button position. 
"""
from pynput.mouse import Listener, Button
import pyautogui as PYG
import HandleStr as strManager
import Coordination as CorManager
from Actions import Scroll_Target,Click_Target,Wait_Target,Drag_Target
from Actions import HandleChinese, isChinese, Process_Checker
from ObjChecker import ObjChecker

""" Action Checker """
Checker = ObjChecker(wait_sec=0.1,timeout=120)

class Spots:

    def __init__(self,spotName,filter=None,filter_parameter=None,channel=-1) -> None:
        self._recordX = -1
        self._recordY = -1
        self._parameterX = -1
        self._parameterY = -1
        self.spotName = spotName
        self.filter = filter
        self.filter_parameter = filter_parameter
        self.channel = channel
        self.Create_spot()
    
    def on_click(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._recordX = x
            self._recordY = y
            return False
    
    def record_target_POS(self):
        print("Please select next new spot.")
        with Listener(on_click=self.on_click) as listenser:
            listenser.join()

    def on_click_parameters(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._parameterX = x
            self._parameterY = y
            return False
        
    def record_parameters_POS(self):
        print("Please select next new parameters.")
        with Listener(on_click=self.on_click_parameters) as listenser:
            listenser.join()

    def Enter_spot_name(self):
        PYG.moveTo(self._recordX, self._recordY)
        PYG.click(clicks=2, button=strManager.LEFT)
        PYG.hotkey(strManager.CTRL, strManager.A)
        PYG.press(strManager.BACKSPACE)
        PYG.write(self.spotName)
        PYG.press(strManager.ENTER)

    def Create_filter(self,filter,filter_parameter,channel):

        ## Click Create spot
        Click_Create_Filter = Click_Target(target=strManager.CREATE_FILTER_BTN)
        Checker.wait_Action(Click_Create_Filter.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click Create spot
        Click_ADD_Filter = Click_Target(target=strManager.ADD_FILTER_BTN)
        Checker.wait_Action(Click_ADD_Filter.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Wait off progress bar
        Wait_filter_Droplist = Wait_Target(target=strManager.FILTER_DROP_LIST,disappear=False)
        Checker.wait_Action(Wait_filter_Droplist.Wait_Function())
        if timer_ring: return None
        
        """ This section scroll droplist"""
        Scroll_filter_Droplist = Scroll_Target(
            steps = CorManager.Spot_Filters[filter]+channel,
            target_X = Wait_filter_Droplist.PosX,
            target_Y = Wait_filter_Droplist.PosY,
            offsetX = -30, offsetY = 0
        )
        Checker.wait_Action(Scroll_filter_Droplist.Scrolling_Function())
        if timer_ring: return None

        ## Click Create spot
        Click_Change_Filter = Click_Target(target=strManager.FILTER_PARAMETER,click=3,offsetX=100)
        Checker.wait_Action(Click_Change_Filter.Click_Function())
        PYG.write(str(filter_parameter))
        PYG.press(strManager.ENTER)

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click Create spot
        Click_Dup_Filter_Spot = Click_Target(target=strManager.DUPLICATE_FILTERED_SPOT_BTN)
        Checker.wait_Action(Click_Dup_Filter_Spot.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Change name of filtered spot
        PYG.moveTo(x=self._recordX+0,y=self._recordY+15,duration=0.2)
        PYG.click(clicks=2)
        PYG.hotkey(strManager.CTRL,strManager.A,strManager.BACKSPACE)
        PYG.write(self.spotName+"_"+strManager.INTENSITY_SUM)
        PYG.press(strManager.ENTER)

    def Create_spot(self):

        ## Click Create spot
        Click_Create_Spot = Click_Target(target=strManager.CREATE_SPOT)
        Checker.wait_Action(Click_Create_Spot.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Generate spots
        self.record_target_POS()
        self.Enter_spot_name()

        ## Click drop list
        Click_Drop_list = Click_Target(
            target=strManager.DROPLIST_ICON,
            offsetX=CorManager.Drop_list_offsetX
        )
        Checker.wait_Action(Click_Drop_list.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Record parameters coordinate
        self.record_parameters_POS()

        ## Click Run program
        Click_RUN_btn = Click_Target(
        target=strManager.RUN_BTN_ICON,
        offsetX=CorManager.RUN_btn_offsetX
        )
        Checker.wait_Action(Click_RUN_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Wait off progress bar
        Wait_Progress_bar = Wait_Target(target=strManager.PROGRESS_BAR,disappear=True)
        Checker.wait_Action(Wait_Progress_bar.Wait_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Create filter
        if self.filter and self.filter_parameter and self.channel >= 0:
            self.Create_filter(filter=self.filter,filter_parameter=self.filter_parameter,channel=self.channel)

        return self

    def Print_Info(self):
        print("Spot name:{} X:{} Y:{}".format(self.spotName,self._recordX,self._recordY))
        print("Filter:{} parameter = {}".format(self.filter,self.filter_parameter))
        print("Channel:{}".format(self.channel))
        print("Spot name:{} para_X:{} para_Y:{}".format(self.spotName,self._parameterX,self._parameterY))

class Colocalize:

    def __init__(self,name,savingDIR) -> None:
        self._targetA_PosX = -1
        self._targetA_PosY = -1
        self._targetB_PosX = -1
        self._targetB_PosY = -1
        self._target_Drag_X = -1
        self._target_Drag_Y = -1
        self.name = name
        self.savingDIR = savingDIR
        self.Create_Colocalize()

    def record_targetA_POS(self):
        print("Please select colocalize targetA.")
        with Listener(on_click=self.on_clickA) as listenser:
            listenser.join()

    def on_clickA(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._targetA_PosX = x
            self._targetA_PosY = y
            return False
    
    def record_targetB_POS(self):
        print("Please select colocalize targetB.")
        with Listener(on_click=self.on_clickB) as listenser:
            listenser.join()

    def on_clickB(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._targetB_PosX = x
            self._targetB_PosY = y
            return False

    def record_Drag_POS(self):
        print("Please select colocalize to drag.")
        with Listener(on_click=self.on_click_Drag) as listenser:
            listenser.join()

    def on_click_Drag(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._target_Drag_X = x
            self._target_Drag_Y = y
            return False

    def Enter_colocalize_name(self,x,y,offsetX=0,offsetY=0):
        PYG.moveTo(x+offsetX,y+offsetY)
        PYG.click(clicks=2, button=strManager.LEFT)
        PYG.hotkey(strManager.CTRL, strManager.A)
        PYG.press(strManager.BACKSPACE)
        PYG.write(self.name)
        PYG.press(strManager.ENTER)

    """ This section create colocalize """
    def Create_Colocalize(self):

        ## Click colocalize-1 
        Click_MENU_btn =  Click_Target(target=strManager.MENU_BTN,duration=0.1)
        Checker.wait_Action(Click_MENU_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None
        
        ## Click colocalize-2
        Click_spotFunc_btn =  Click_Target(target=strManager.SPOT_FUNC_BTN)
        Checker.wait_Action(Click_spotFunc_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click colocalize-3
        Click_Colocalize_btn =  Click_Target(target=strManager.COLOCALIZE_BTN,duration=0.2)
        Checker.wait_Action(Click_Colocalize_btn.Click_Function())
        
        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click colocalize-4
        Wait_colocalize_window = Wait_Target(target=strManager.COLOCALIZE_WINDOW,disappear=False)
        Checker.wait_Action(Wait_colocalize_window.Wait_Function())
        
        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None
        
        # Create colocalize
        self.record_targetA_POS()
        self.record_targetB_POS()

        """ This section click ok on colocalize window"""
        Click_colocalize_windowOK = Click_Target(
            target=strManager.COLOCALIZE_WINDOW,
            offsetX=CorManager.COLOCALIZE_WINDOW_OK_offsetX,
            offsetY=CorManager.COLOCALIZE_WINDOW_OK_offsetY
        )
        Checker.wait_Action(Click_colocalize_windowOK.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        """ This section wait out colocalize window """
        Wait_colocalize_ratio_OK_btn =  Wait_Target(target=strManager.COLOCALIZE_RATIO_OK_BTN)
        Checker.wait_Action(Wait_colocalize_ratio_OK_btn.Wait_Function())
        
        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        """ This section Enter 0.5 on text box """
        PYG.press(strManager.BACKSPACE)

        ## Click off Chinese typer
        if isChinese(): click_check = HandleChinese()
        Processing = Process_Checker(click_check)
        if not Processing: return None

        # Need to add offset to Manager
        PYG.write(strManager.COLOCALIZE_RATIO)
        Click_colocalize_ratio_OK_btn =  Click_Target(
            target = strManager.COLOCALIZE_RATIO_OK_BTN,
            offsetX = -60, offsetY = 25
        )
        Checker.wait_Action(Click_colocalize_ratio_OK_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        """ This section determine if there is any colocalize """
        # Devoloping

        """ This section wait off co-localize matlab window """
        Wait_matLAB_window_off = Wait_Target(target=strManager.MATLAB_WINDOW,disappear=True)
        Checker.wait_Action(Wait_matLAB_window_off.Wait_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        """ Close opened folder """
        ## Click off opened folder
        Click_Open_folder =  Click_Target(target=strManager.CLOSE_FOLDER_BTN,offsetX=-10)
        Checker.wait_Action(Click_Open_folder.Click_Off_Function())
        PYG.click(clicks=2)

        """ This section drag colocalize to outside below DAPI"""
        self.record_Drag_POS()

        """ This section find hierarchy icon """
        Wait_hierarchy = Wait_Target(target=strManager.HIERARCHY_ICON,disappear=False)
        Checker.wait_Action(Wait_hierarchy.Wait_Function())
        
        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        """ This section drag colocalize spot to outside """
        # Need to add offset to Manager
        hierarchy_offsetX = 0
        hierarchy_offsetY = 0
        colocalize_spot_X = Wait_hierarchy.PosX + hierarchy_offsetX
        colocalize_spot_Y = Wait_hierarchy.PosY + hierarchy_offsetY
        Drag_APB = Drag_Target(
            target_X = self._target_Drag_X,
            target_Y = self._target_Drag_Y,
            to_X = colocalize_spot_X, 
            to_Y = colocalize_spot_Y,
            duration=0.25
        )
        Checker.wait_Action(Drag_APB.Drag_Function())

        """ This section Enter colocalize name """
        ## Click off Chinese typer
        if isChinese(): click_check = HandleChinese()
        Processing = Process_Checker(click_check)
        if not Processing: return None

        self.Enter_colocalize_name(
            x = colocalize_spot_X,
            offsetX = 0,
            y = colocalize_spot_Y,
            offsetY = 0
        )

        ## Click split spot to surface 1 
        Click_MENU_btn =  Click_Target(target=strManager.MENU_BTN)
        Checker.wait_Action(Click_MENU_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click split spot to surface 2
        Click_spotFunc_btn =  Click_Target(target=strManager.SPOT_FUNC_BTN)
        Checker.wait_Action(Click_spotFunc_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click split spot to surface 3 
        Click_Split_spot_to_surface =  Click_Target(target=strManager.SPLT_SPOT_TO_SURFACE)
        Checker.wait_Action(Click_Split_spot_to_surface.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Wait out spliting window
        Wait_Spliting = Wait_Target(target=strManager.SPLITING_WINDOW,disappear=False)
        Checker.wait_Action(Wait_Spliting.Wait_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Wait out matlab window
        Wait_matLAB_window_out = Wait_Target(target=strManager.SPLITING_WINDOW,disappear=False)
        Checker.wait_Action(Wait_matLAB_window_out.Wait_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Wait off matlab window
        Wait_matLAB_window_off = Wait_Target(target=strManager.MATLAB_WINDOW,disappear=True)
        Checker.wait_Action(Wait_matLAB_window_off.Wait_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click off opened folder
        Click_Open_folder =  Click_Target(target=strManager.CLOSE_FOLDER_BTN,offsetX=-10)
        Checker.wait_Action(Click_Open_folder.Click_Off_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Rename colocalize folder
        Wait_inside_surface = Wait_Target(target=strManager.INSIDE_SURFACE,disappear=False)
        Checker.wait_Action(Wait_inside_surface.Wait_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        self.Enter_colocalize_name(
            x = Wait_inside_surface.PosX,
            y = Wait_inside_surface.PosY,
        )

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click statistic button
        Click_Statics_btn =  Click_Target(target=strManager.STATISTIC_BTN)
        Checker.wait_Action(Click_Statics_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click Overall button
        # Need to add offset to Manager
        Click_Overall_btn =  Click_Target(target=strManager.OVERALL_BTN, offsetY = 25)
        Checker.wait_Action(Click_Overall_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click Export
        Click_Export_btn =  Click_Target(target=strManager.EXPORT_BTN, offsetX = -5)
        Checker.wait_Action(Click_Export_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Enter Export path
        Click_Saving_DIR =  Click_Target(target=strManager.SAVING_DIR, offsetX = -50,str=self.savingDIR)
        Checker.wait_Action(Click_Saving_DIR.Click_Enter_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        ## Click SAVE
        Click_Save_btn =  Click_Target(target=strManager.SAVE_BTN, offsetX = -120)
        Checker.wait_Action(Click_Save_btn.Click_Function())

        ## process checker
        timer_ring = Checker.checkTime()
        if timer_ring: return None

        return self

    def Print_Info(self):
        print("Colocalize name:{} spotA_X:{} spotA_Y:{}".format(self.name,self._targetA_PosX,self._targetA_PosY))
        print("Colocalize name:{} spotB_X:{} spotB_Y:{}".format(self.name,self._targetB_PosX,self._targetB_PosY))
        print("Colocalize name:{} Drag_X:{} Drag_Y:{}".format(self.name,self._target_Drag_X,self._target_Drag_Y))
        print("Colocalize name:{} Save to :{}".format(self.name,self.savingDIR))

if __name__ == "__main__":
    print("Create spots and colocalize events")
