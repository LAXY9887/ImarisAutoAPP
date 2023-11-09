import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 3

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = strManager.INTENSITY_SUM
TRF2_filter_parameter = 1300
TRF2_channel_IDX = 1

## BRCA1
BRCA1_Id = "BRCA1"
BRCA1_filter = None
BRCA1_filter_parameter = None
BRCA1_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:{
        strManager.STR_FILTER : TRF2_filter,
        strManager.STR_FILTER_PARAMETER : TRF2_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    BRCA1_Id :{
        strManager.STR_FILTER : BRCA1_filter,
        strManager.STR_FILTER_PARAMETER : BRCA1_filter_parameter,
        strManager.STR_CHANNEL_IDX : BRCA1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}


""" Split spot object """
totalBRCA1_Id = "BRCA1"
OutputDIR_totalBRCA1 = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_07_U2OS KD TIRR rep3 IF BRCA1-TRF2\total BRCA1"

""" Split spot dict """
SplitingID_dict = {
    totalBRCA1_Id : {strManager.STR_SPLIT_OUTDIR : OutputDIR_totalBRCA1}
}

""" Colocalize variables """
## TRF2_BRCA1
Clocal_Id = "TRF2_BRCA1"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_07_U2OS KD TIRR rep3 IF BRCA1-TRF2\5%TRF2 BRCA1 foci"
Clocal_sec_colocalize = None
OutputDIR_Clocal_sec_colocalize = None

## total TRF2_BRCA1
Clocal_Id2 = "totalTRF2_BRCA1"
OutputDIR_Clocal2 = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_07_U2OS KD TIRR rep3 IF BRCA1-TRF2\total TRF2 BRCA1 foci"
Clocal_sec_colocalize2 = None
OutputDIR_Clocal_sec_colocalize2 = None

ColocalizeID_dict = {
    Clocal_Id:{
        strManager.STR_COL_OUT_DIR : OutputDIR_Clocal,
        strManager.STR_SEC_COL : Clocal_sec_colocalize,
        strManager.STR_SEC_COL_OUT_DIR : OutputDIR_Clocal_sec_colocalize,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    Clocal_Id2:{
        strManager.STR_COL_OUT_DIR : OutputDIR_Clocal2,
        strManager.STR_SEC_COL : Clocal_sec_colocalize2,
        strManager.STR_SEC_COL_OUT_DIR : OutputDIR_Clocal_sec_colocalize2,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}

""" Working dir """
targetDIR = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_07_U2OS KD TIRR rep3 IF BRCA1-TRF2"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\HNG IMS export"