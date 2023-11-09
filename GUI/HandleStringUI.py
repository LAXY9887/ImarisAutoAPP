import os

""" Asset path """
assetDir = ".\AssetUI"

""" Font """
ARIAL = "Arial"

""" Spot ID label """
SPOT_ID_LABEL = "Spot ID:"

""" Add Panned Window Btn Text """
ADDONE = "Add a New"

""" Images assets """
## Spot icon
SPOT_ICON_1 = "Spot icon1.png"
SPOT_ICON_2 = "Spot icon2.png"

## Delete spot btn
DELETE_SPOT_BTN = "Delete spot button.png"

def getAssetUI(asset):
    return os.path.join(assetDir,asset)

if __name__ == '__main__':
    print("Handle string in UI")