import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 2

""" Spots Variables """
## POT1
POT1_Id = "POT1"
POT1_filter = None
POT1_filter_parameter = None
POT1_channel_IDX = -1

## TELOC
TELOC_Id = "TELOC"
TELOC_filter = None
TELOC_filter_parameter = None
TELOC_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    POT1_Id:{
        strManager.STR_FILTER : POT1_filter,
        strManager.STR_FILTER_PARAMETER : POT1_filter_parameter,
        strManager.STR_CHANNEL_IDX : POT1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    TELOC_Id :{
        strManager.STR_FILTER : TELOC_filter,
        strManager.STR_FILTER_PARAMETER : TELOC_filter_parameter,
        strManager.STR_CHANNEL_IDX : TELOC_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}


""" Split spot object """
total_Id = ""
OutputDIR_total = ""

""" Split spot dict """
SplitingID_dict = {
    #total_Id : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total}
}

""" Colocalize variables """
## POT1_TELOC
Clocal_Id = "POT1_TELOC"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\KaLok\20231013 mESC 3rd run DNA FISH POT1(cy3) TeloC (FITC)\colocalization"
Clocal_sec_colocalize = None
OutputDIR_Clocal_sec_colocalize = None

ColocalizeID_dict = {
    Clocal_Id:{
        strManager.STR_COL_OUT_DIR : OutputDIR_Clocal,
        strManager.STR_SEC_COL : Clocal_sec_colocalize,
        strManager.STR_SEC_COL_OUT_DIR : OutputDIR_Clocal_sec_colocalize,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}

""" Working dir """
targetDIR = r"C:\Users\Imaris\Desktop\imaris KaLok"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\imaris KaLok processed\20231013 mESC 3rd run DNA FISH POT1(cy3) TeloC (FITC)"