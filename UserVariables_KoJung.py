import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 3

""" Spots Variables """
## wdr82
wdr82_Id = "wdr"
wdr82_filter = None
wdr82_filter_parameter = None
wdr82_channel_IDX = -1

## RNApS5
RNApS5_Id = "pS5"
RNApS5_filter = None
RNApS5_filter_parameter = None
RNApS5_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    wdr82_Id:{
        strManager.STR_FILTER : wdr82_filter,
        strManager.STR_FILTER_PARAMETER : wdr82_filter_parameter,
        strManager.STR_CHANNEL_IDX : wdr82_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    RNApS5_Id :{
        strManager.STR_FILTER : RNApS5_filter,
        strManager.STR_FILTER_PARAMETER : RNApS5_filter_parameter,
        strManager.STR_CHANNEL_IDX : RNApS5_channel_IDX,
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
## wdr82_RNApS5
Clocal_Id = "wdr_pS5"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\YCP\20230920 IF wdr82 RNAPs5\colocalization result\output"
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
targetDIR = r"\\DS918\R807_data\LAB member\YCP\20230920 IF wdr82 RNAPs5\quantification"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\YCP\20230920 IF wdr82 RNAPs5\colocalization result\excel"