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
total_Id = ""
OutputDIR_total = ""

""" Split spot dict """
SplitingID_dict = {
    #total_Id : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total}
}

""" Colocalize variables """
## TRF2_PML
Clocal_Id = "TRF2_PML"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Jenny\U2OS inducibly express RNaseH1 data\TRF2-PML\TRF2-PLM_tRWT1 WTA1_Rep1_20230630\_0excel"
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
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\imaris KaLok processed\test"