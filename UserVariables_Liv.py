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

## XPF
XPF_Id = "XPF"
XPF_filter = None
XPF_filter_parameter = None
XPF_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:{
        strManager.STR_FILTER : TRF2_filter,
        strManager.STR_FILTER_PARAMETER : TRF2_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    XPF_Id :{
        strManager.STR_FILTER : XPF_filter,
        strManager.STR_FILTER_PARAMETER : XPF_filter_parameter,
        strManager.STR_CHANNEL_IDX : XPF_channel_IDX,
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
## TRF2_XPF
Clocal_Id = "TRF2_XPF"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Liv\20230704_tetON_U2OS+Lur_XPF and TRF2\Excel"
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
targetDIR = r"\\DS918\R807_data\LAB member\Liv\20230704_tetON_U2OS+Lur_XPF and TRF2\surface"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Liv\20230704_tetON_U2OS+Lur_XPF and TRF2\IMS_Processed"