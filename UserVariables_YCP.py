import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 2

""" Spots Variables """
## RNA pol2
RNApol2_Id = "RNA pol2"
RNApol2_filter = None
RNApol2_filter_parameter = None
RNApol2_channel_IDX = -1

## wdr82
wdr82_Id = "wdr82"
wdr82_filter = None
wdr82_filter_parameter = None
wdr82_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    RNApol2_Id:{
        strManager.STR_FILTER : RNApol2_filter,
        strManager.STR_FILTER_PARAMETER : RNApol2_filter_parameter,
        strManager.STR_CHANNEL_IDX : RNApol2_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    wdr82_Id :{
        strManager.STR_FILTER : wdr82_filter,
        strManager.STR_FILTER_PARAMETER : wdr82_filter_parameter,
        strManager.STR_CHANNEL_IDX : wdr82_channel_IDX,
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
## RNApol2_wdr82
Clocal_Id = "RNApol2_wdr82"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\YCP\20231115 IF wdr82_D2138 RNAPs5_61986\quantification\colocalization"
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
targetDIR = r"C:\Users\Imaris\Desktop\imaris YCP\target"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\imaris YCP\processed"