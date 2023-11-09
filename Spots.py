from pynput.mouse import Listener, Button
import pyautogui as PYG
import HandleStr as strManager
import Coordination as CorManager
from Coordination import Point
import Actions
ActionManager = Actions.handleTarget()

class Spots:

    def __init__(self,spotName,total_channel,filter=None,filter_parameter=None,channel=-1) -> None:
        self._recordPoint = Point()
        self._parameterPoint = Point()
        self.spotName = spotName
        self.total_channel = total_channel
        self.filter = filter
        self.filter_parameter = filter_parameter
        self.channel = channel
        self.Create_spot()
    
    def on_click(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._recordPoint.setPoint(x,y)
            return False
    
    def record_target_POS(self):
        print("Please select next new spot.")
        with Listener(on_click=self.on_click) as listenser:
            listenser.join()
    
    def click_target_POS(self):
        PYG.moveTo(self._recordPoint.x, self._recordPoint.y)
        PYG.click(clicks=1, button=strManager.LEFT)

    def on_click_parameters(self,x, y, button, is_press):
        if button == Button.left and is_press:
            self._parameterPoint.setPoint(x,y)
            return False
        
    def record_parameters_POS(self):
        print("Please select next new parameters.")
        with Listener(on_click=self.on_click_parameters) as listenser:
            listenser.join()

    def click_parameters_POS(self):
        PYG.moveTo(self._parameterPoint.x,self._parameterPoint.y,duration=0.2)
        PYG.click(clicks=1, button=strManager.LEFT)

    def Enter_spot_name(self):
        PYG.moveTo(self._recordPoint.x, self._recordPoint.y)
        PYG.click(clicks=2, button=strManager.LEFT)
        PYG.hotkey(strManager.CTRL, strManager.A)
        PYG.press(strManager.BACKSPACE)
        PYG.write(self.spotName)
        PYG.press(strManager.ENTER)

    def Create_filter(self,filter,filter_parameter,channel,total_ch):

        ## Click Create spot
        ActionManager.click_target(target=strManager.CREATE_FILTER_BTN)

        ## Click Create spot
        ActionManager.click_target(target=strManager.ADD_FILTER_BTN)

        ## Scrolling filter
        ActionManager.scroll_target(
            target =strManager.FILTER_DROP_LIST,
            steps = CorManager.Base_filter_idx + (total_ch * CorManager.Spot_Filters[filter]) + channel,
            offset = CorManager.Spot_filter_offset
            )

        ## Click Create spot
        ActionManager.click_target(target = strManager.FILTER_PARAMETER,
            click = 3, offset = CorManager.Filter_parameterBOX_offset
        )
        PYG.write(str(filter_parameter))
        PYG.press(strManager.ENTER)

        ## Click Create spot
        ActionManager.click_target(target=strManager.DUPLICATE_FILTERED_SPOT_BTN)

        ## Change name of filtered spot
        PYG.moveTo(x=self._recordPoint.x+0,y=self._recordPoint.y+15,duration=0.2)
        PYG.click(clicks=2)
        PYG.hotkey(strManager.CTRL,strManager.A,strManager.BACKSPACE)
        PYG.write(self.spotName+"_"+strManager.INTENSITY_SUM)
        PYG.press(strManager.ENTER)

    def Create_spot(self):
        
        """ 0X. Check & Click off Chinese Typer """
        if Actions.isChinese(): Actions.HandleChinese()

        ## Click Create spot
        ActionManager.click_target(target=strManager.CREATE_SPOT)

        ## Generate spots
        if not self._recordPoint.isSet():
            self.record_target_POS()
        else:
            self.click_target_POS()
        self.Enter_spot_name()

        ## Click drop list
        ActionManager.click_target(target=strManager.DROPLIST_ICON,offset=CorManager.Drop_list_offset)

        ## Record parameters coordinate
        if not self._parameterPoint.isSet():
            self.record_parameters_POS()
        else:
            self.click_parameters_POS()

        ## Click Run program
        ActionManager.click_target(strManager.RUN_BTN_ICON,offset=CorManager.RUN_btn_offset)

        ## Wait off progress bar
        ActionManager.WaitOff_target(target=strManager.PROGRESS_BAR)

        ## Create filter
        if self.filter and self.filter_parameter and self.channel >= 0:
            self.Create_filter(filter=self.filter,filter_parameter=self.filter_parameter,channel=self.channel,total_ch=self.total_channel)

        return self

    def Print_Info(self):
        print("Spot name:{} Position:{}".format(self.spotName,self._recordPoint.showPoint()))
        print("Filter:{} parameter = {}".format(self.filter,self.filter_parameter))
        print("Channel:{}".format(self.channel))
        print("Spot name:{} Parameter:{}".format(self.spotName,self._parameterPoint.showPoint()))
    
if __name__ == "__main__":
    print("Spot Object")