import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 4

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = None
TRF2_filter_parameter = None
TRF2_channel_IDX = -1

## STN1
STN1_Id = "STN1"
STN1_filter = None
STN1_filter_parameter = None
STN1_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:{
        strManager.STR_FILTER : TRF2_filter,
        strManager.STR_FILTER_PARAMETER : TRF2_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    STN1_Id :{
        strManager.STR_FILTER : STN1_filter,
        strManager.STR_FILTER_PARAMETER : STN1_filter_parameter,
        strManager.STR_CHANNEL_IDX : STN1_channel_IDX,
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
## TRF2_STN1
Clocal_Id = "TRF2_STN1"
# 輸入 Export 的 excel 路徑
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Elaine\20230207 IF_mES Scr.small TERRA (20220213 sample)_STN1.TRF2, POT1.TRF1\Imaris quant excel\STN1 TRF2"
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
targetDIR = r"\\DS918\R807_data\LAB member\Elaine\20230207 IF_mES Scr.small TERRA (20220213 sample)_STN1.TRF2, POT1.TRF1\Imaris DAPI cropped file\STN1 TRF2"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Elaine\20230207 IF_mES Scr.small TERRA (20220213 sample)_STN1.TRF2, POT1.TRF1\Imaris processed file\STN1 TRF2"