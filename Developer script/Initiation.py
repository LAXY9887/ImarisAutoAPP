import subprocess
import pyautogui as PYG
import os
import ObjChecker as Checker
import HandleStr as strManager

""" Variables """
targetDIR = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_06_U2OS KD TIRR rep2 IF APBs"
targetFILE = r"U2OS TIRR KD rep2 s38882 APBs_06_Multichannel Z-Stack_20220627_58898.ims"
full_targetPath = os.path.join(targetDIR,targetFILE)

""" This section initiate Imaris """
initial_ERROR = strManager.getAsset(strManager.ERROR_ICON)
subprocess.Popen([strManager.IMARIS_DIR,full_targetPath])

""" This section wait for initial error and click it off """
def find_Initial_ERROR():
    offsetX, offsetY = (346,44)
    initial_ERROR_loc = PYG.locateCenterOnScreen(initial_ERROR)
    if initial_ERROR_loc != None:
        PYG.moveTo(initial_ERROR_loc.x+offsetX, initial_ERROR_loc.y+offsetY)
        PYG.click(clicks=1, button='left')
        return True
    return None

Checker.wait_Action(find_Initial_ERROR)

if __name__ == "__name__":
    print("Initialize Imaris Development script.")