import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 3

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = None
TRF2_filter_parameter = None
TRF2_channel_IDX = -1

## BRAC1
BRAC1_Id = "BRAC1"
BRAC1_filter = None
BRAC1_filter_parameter = None
BRAC1_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:{
        strManager.STR_FILTER : TRF2_filter,
        strManager.STR_FILTER_PARAMETER : TRF2_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    BRAC1_Id :{
        strManager.STR_FILTER : BRAC1_filter,
        strManager.STR_FILTER_PARAMETER : BRAC1_filter_parameter,
        strManager.STR_CHANNEL_IDX : BRAC1_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}


""" Split spot object """
total_Id = "total TRF2"
OutputDIR_total = r"\\DS918\R807_data\LAB member\Chia\2023.01.27_U2OS_KD-DHX8_protein staining\0_complete BRAC1\total TRF2"

""" Split spot dict """
SplitingID_dict = {
    total_Id : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total}
}

""" Colocalize variables """
## TRF2_RNH
Clocal_Id = "T2BC1"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Chia\2023.01.27_U2OS_KD-DHX8_protein staining\0_complete BRAC1\colocalize"
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
targetDIR = r"\\DS918\R807_data\LAB member\Chia\2023.01.27_U2OS_KD-DHX8_protein staining\BRAC1-TRF2\surface completed"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Chia\2023.01.27_U2OS_KD-DHX8_protein staining\0_complete BRAC1\for imaris"