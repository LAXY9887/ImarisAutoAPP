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

## RNH
RNH_Id = "RNH"
RNH_filter = None
RNH_filter_parameter = None
RNH_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:{
        strManager.STR_FILTER : TRF2_filter,
        strManager.STR_FILTER_PARAMETER : TRF2_filter_parameter,
        strManager.STR_CHANNEL_IDX : TRF2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    RNH_Id :{
        strManager.STR_FILTER : RNH_filter,
        strManager.STR_FILTER_PARAMETER : RNH_filter_parameter,
        strManager.STR_CHANNEL_IDX : RNH_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    }
}


""" Split spot object """
total_Id = "total TRF2"
OutputDIR_total = r"\\DS918\R807_data\LAB member\Chia\2022.11.25_U2OS_Lur(time)_GSTtag-Rloop(b)&TRF2(r)_rep2\only TRF2 excel"

""" Split spot dict """
SplitingID_dict = {
    total_Id : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total}
}

""" Colocalize variables """
## TRF2_RNH
Clocal_Id = "TRF2_RNH"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Chia\2022.11.25_U2OS_Lur(time)_GSTtag-Rloop(b)&TRF2(r)_rep2\RNH-TRF2 colocalization excel"
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
targetDIR = r"C:\Users\Imaris\Desktop\CHIA 12.12 GST-TRF2(R2)"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\export GST-TRF2"