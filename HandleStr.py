import os

""" Critical Dir """
IMARIS_DIR = r"C:\Program Files\Bitplane\Imaris x64 9.2.1\Imaris.exe"
ASSET_DIR = r".\Assets"

""" Keyboard """
LEFT = 'left'
RIGHT = 'right'
CTRL = 'ctrl'
A = 'a'
BACKSPACE = 'backspace'
ENTER = 'enter'

""" Name """
INITIAL_ERROR = "initial error.png"
ERROR_ICON = "error.png"
CREATE_SPOT = "create spot.png"
TYPE_MODE_ICON = "type mode.png"
DROPLIST_ICON = "drop list icon.png"
RUN_BTN_ICON = "run button.png"
MENU_BTN = "menu buttons.png"
SPOT_FUNC_BTN = "spot function button.png"
PROGRESS_BAR = "progress bar.png"
PROGRESS_BAR_CANCEL_BTN = "progress bar cancel btn.png"
COLOCALIZE_BTN = "colocalize spot button.png"
COLOCALIZE_WINDOW = "colocalize function window.png"
COLOCALIZE_RATIO_OK_BTN = "colocalize ratio button.png"
COLOCALIZE_WINDOW_STRING = "colocalize window string.png"
HIERARCHY_ICON = "hierarchy icon.png"
HIERARCHY_ICON2 = "hierarchy icon2.png"
SPLT_SPOT_TO_SURFACE = "split spot to surface.png"
CLOSE_FOLDER_BTN = "close folder button.png"
CLOSE_FOLDER_BTN_LONG = "close folder button long.png"
CLOSE_FOLDER_BTN_EX_LONG = "close folder button ex long.png"
INSIDE_SURFACE = "inside surface.png"
STATISTIC_BTN = "statics button.png"
OVERALL_BTN = "overall button.png"
EXPORT_BTN = "export button.png"
SAVING_DIR = "saving directory.png"
SAVE_BTN = "saving button.png"
MATLAB_WINDOW = "matlab windiw.png"
SPLITING_WINDOW = "Spliting spot window.png"
EXPORT_IMS_BTN = "Export IMS button.png"
EXPORT_IMS_WINDOW = "Exporting IMS window.png"
CLOSE_IMARIS_BTN = "close imaris button.png"
CREATE_FILTER_BTN = "create filter button.png"
ADD_FILTER_BTN = "Add filter button.png"
FILTER_DROP_LIST = "filter drop list.png"
FILTER_PARAMETER = "filter parameter box.png"
DUPLICATE_FILTERED_SPOT_BTN = "duplicate selection.png"
RENAME_COLOCALIZE_TARGET = "Rename colocalize target.png"
IMARIS_ICON = "imaris icon.png"
NO_COLOCALIZE_WINDOW = "No colocalize spot window.png"
BAD_SUBSCRIPT = "bad subscript window.png"
SPLIT_SPOT_CLOSE = "split spot close window.png"
CREATE_FOLDER_BTN = "create folder button.png"
NEW_FOLDER = "NewFolder.png"
NEWSPOT_FOLDER = "new spot folder.png"
EXIST_EXCEL_SIGN = "existing excel sign.png"
EXIST_EXCEL_YES_BTN = "existing excel yes button.png"
SCROLL_BAR = "scroll bar.png"
SCROLL_BAR_TOP = "scroll bar top.png"
OVERWRITE_IMS = "over write ims icon.png"
OVERWRITE_IMS_YES_BTN = "over write ims yes button.png"
CLOSE_EXCEL_BTN = "close excel button.png"
CLOSE_EXCEL_BTN_POPUP = "close excel button popup.png"
IMARIS_ICON = "ims icon.png"
EXCEL_SAVE= "excel save btn.png"

""" NEW folder name """
SPOT_FOLDER_NAME = "CreateSpots"

""" Spot parameter """
STR_FILTER = "filter"
STR_FILTER_PARAMETER = "filter_parameter"
STR_CHANNEL_IDX = "channel_IDX"
STR_TOTAL_CH_NUM = "total_channel_number"

""" Spliting spots parameter """
STR_SPLIT_OUTDIR = "OutputDIR_spliting"

""" colocalize parameter """
STR_COL_OUT_DIR = "OutputDIR_Clocal"
STR_SEC_COL = "Clocal_sec_colocalize"
STR_SEC_COL_OUT_DIR = "OutputDIR_Clocal_sec_colocalize"
COLOCALIZE_RATIO = "0.4"

""" spots filter """
INTENSITY_SUM = 'Intensity_sum'

def getAsset(assaet):
        fullpath = os.path.join(ASSET_DIR,assaet)
        return fullpath

if __name__ == "__main__":
    print("Record of strings")