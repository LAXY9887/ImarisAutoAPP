import HandleStr as strManager

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

    def showPoint(self):
        return (self.x,self.y)

""" Find Initial ERROR """
Initial_ERROR_offset = Point(346,44)

""" Find Drop list"""
Drop_list_offset = Point(-50,0)

""" Find RUN button """
RUN_btn_offset = Point(15,0)

""" Spot filter list """
Spot_filter_offset = Point(-30,0)
Filter_parameterBOX_offset = Point(100,0)

""" Find OK on colocalize window """
COLOCALIZE_WINDOW_OK_offset = Point(0,270)
COLOCALIZE_ratio_offset = Point(-60,25)

""" Close no colocalize window"""
NO_COLOCALIZE_window_offset = Point(0,25)

""" Close off opened folder """
CLICK_OFF_FOLDER_BTN_offset = Point(-2,0)
CLICK_OFF_FOLDER_BTN_EX_offset = Point(5,0)
CLICK_OFF_FOLDER_BTN_shift = Point(30,0)

""" Enter colocalize name """
ENTER_colocalize_offset = Point(50,0)

""" Close bad subscript """
CLOSE_BADsubscript_offset = Point(45,-15)

""" Click stastic overll offset """
Overall_btn_offset = Point(0,25)
Export_excel_btn = Point(-5,0)
Enter_export_path = Point(-50,0)
Click_saving_btn_offset = Point(-120,0)

""" Click overwrite imaris file """
OverwriteIMS_offset = Point(430,70)

""" Export ims file """
Export_IMS_window_offset = Point(-15,0)
OverWrite_IMS_OK_offset = Point(415,105)
CLose_imaris_btn_offset = Point(50,0)

""" Scroll bar for spot filter """
#intensity_SUM_idx = 30
Base_filter_idx = 6
intensity_SUM_idx = 6
Spot_Filters = {
    strManager.INTENSITY_SUM : intensity_SUM_idx
}

if __name__ == "__main__":
    print("Record of coordinate")