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

## TRF1
TRF1_Id = "TRF1"
TRF1_filter = None
TRF1_filter_parameter = None
TRF1_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    POT1_Id:{
        strManager.STR_FILTER : POT1_filter,
        strManager.STR_FILTER_PARAMETER : POT1_filter_parameter,
        strManager.STR_CHANNEL_IDX : POT1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    TRF1_Id :{
        strManager.STR_FILTER : TRF1_filter,
        strManager.STR_FILTER_PARAMETER : TRF1_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF1_channel_IDX,
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
## POT1_TRF1
Clocal_Id = "POT1_TRF1"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\KaLok\20221218 mESC POT1 TRF1\re-colocalization for %"
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
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\imaris KaLok processed\20221218 mESC POT1 TRF1"