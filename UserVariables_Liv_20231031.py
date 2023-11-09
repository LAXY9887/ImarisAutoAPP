import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 2

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = None
TRF2_filter_parameter = None
TRF2_channel_IDX = -1

## PML
PML_Id = "PML"
PML_filter = None
PML_filter_parameter = None
PML_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:{
        strManager.STR_FILTER : TRF2_filter,
        strManager.STR_FILTER_PARAMETER : TRF2_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    PML_Id :{
        strManager.STR_FILTER : PML_filter,
        strManager.STR_FILTER_PARAMETER : PML_filter_parameter,
        strManager.STR_CHANNEL_IDX : PML_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}


""" Split spot object """
total_TRF2 = "total TRF2"
OutputDIR_total = r"\\DS918\R807_data\LAB member\Liv\20231024_U2OS+LandA_APB replicate 1\excel\TRF2"

""" Split spot dict """
SplitingID_dict = {
    total_TRF2 : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total}
}

""" Colocalize variables """
## TRF2_PML
Clocal_Id = "TRF2_PML"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Liv\20231024_U2OS+LandA_APB replicate 1\excel\colocalize"
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
targetDIR = r"\\DS918\R807_data\LAB member\Liv\20231024_U2OS+LandA_APB replicate 1\Imris"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Liv\20231024_U2OS+LandA_APB replicate 1\imris final"