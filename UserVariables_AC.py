import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 3

""" Spots Variables """
## TRF1
TRF1_Id = "TRF1"
TRF1_filter = None
TRF1_filter_parameter = None
TRF1_channel_IDX = -1

## TRF2
hTR_Id = "hTR"
hTR_filter = None
hTR_filter_parameter = None
hTR_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF1_Id:{
        strManager.STR_FILTER : TRF1_filter,
        strManager.STR_FILTER_PARAMETER : TRF1_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    hTR_Id :{
        strManager.STR_FILTER : hTR_filter,
        strManager.STR_FILTER_PARAMETER : hTR_filter_parameter,
        strManager.STR_CHANNEL_IDX : hTR_channel_IDX,
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
## TRF1_hTR
Clocal_Id = "TRF1_hTR"
OutputDIR_Clocal = r"\\ds918\R807_data\LAB member\Andrew"
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
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\imaris KaLok processed\20230712 mESC 1st run PNA TRF1 hTR in milk (DNA-FISH) (trial 2 higher thershold)"