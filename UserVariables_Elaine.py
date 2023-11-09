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

## CTC1
CTC1_Id = "CTC1"
CTC1_filter = None
CTC1_filter_parameter = None
CTC1_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF1_Id:{
        strManager.STR_FILTER : TRF1_filter,
        strManager.STR_FILTER_PARAMETER : TRF1_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    CTC1_Id :{
        strManager.STR_FILTER : CTC1_filter,
        strManager.STR_FILTER_PARAMETER : CTC1_filter_parameter,
        strManager.STR_CHANNEL_IDX : CTC1_channel_IDX,
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
## TRF1_CTC1
Clocal_Id = "TRF1_CTC1"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Elaine\20221108 IF_mES small TERRA (20220213 sample)\Imaris quant\CTC1_TRF1"
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
targetDIR = r"C:\Users\Imaris\Desktop\Imaris DAPI Crop\CTC1 TRF1_2"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\Imaris processed file\CTC1_TRF1_v1"