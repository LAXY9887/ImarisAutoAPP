import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 4

""" Spots Variables """
## TRF1
TRF1_Id = "TRF1"
TRF1_filter = None
TRF1_filter_parameter = None
TRF1_channel_IDX = -1

## POT1
POT1_Id = "POT1"
POT1_filter = None
POT1_filter_parameter = None
POT1_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF1_Id:{
        strManager.STR_FILTER : TRF1_filter,
        strManager.STR_FILTER_PARAMETER : TRF1_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    POT1_Id :{
        strManager.STR_FILTER : POT1_filter,
        strManager.STR_FILTER_PARAMETER : POT1_filter_parameter,
        strManager.STR_CHANNEL_IDX : POT1_channel_IDX,
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
## TRF1_POT1
Clocal_Id = "TRF1_POT1"
# 輸入 Export 的 excel 路徑
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Elaine\20230207 IF_mES Scr.small TERRA (20220213 sample)_STN1.TRF2, POT1.TRF1\Imaris quant excel\POT1 TRF1"
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
targetDIR = r"\\DS918\R807_data\LAB member\Elaine\20230207 IF_mES Scr.small TERRA (20220213 sample)_STN1.TRF2, POT1.TRF1\Imaris DAPI cropped file\POT1 TRF1"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Elaine\20230207 IF_mES Scr.small TERRA (20220213 sample)_STN1.TRF2, POT1.TRF1\Imaris processed file\POT TRF1"