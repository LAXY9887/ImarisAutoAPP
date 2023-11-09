import pyautogui as PYG
import HandleStr as strManager

""" This section initiate Imaris. """
def find_Initial_ERROR():
    offsetX, offsetY = (346,44)
    initial_ERROR = strManager.getAsset(strManager.ERROR_ICON)
    initial_ERROR_loc = PYG.locateCenterOnScreen(initial_ERROR)
    if initial_ERROR_loc != None:
        PYG.moveTo(initial_ERROR_loc.x+offsetX, initial_ERROR_loc.y+offsetY)
        PYG.click(clicks=1, button='left')
        return True
    return None

""" This section click create spot. """
def Click_Create_Spot():
    create_spot = strManager.getAsset(strManager.CREATE_SPOT)
    create_spot_loc = PYG.locateCenterOnScreen(create_spot)
    if create_spot_loc != None:
        PYG.moveTo(create_spot_loc.x, create_spot_loc.y)
        PYG.click(clicks=1, button='left')
        return True
    return None

""" This section click Type mode button. """
def Click_Type_Mode():
    type_mode = strManager.getAsset(strManager.TYPE_MODE_ICON)
    type_mode_loc = PYG.locateCenterOnScreen(type_mode)
    if type_mode_loc != None:
        PYG.moveTo(type_mode_loc.x, type_mode_loc.y)
        PYG.click(clicks=1, button='left')
        return True
    return None