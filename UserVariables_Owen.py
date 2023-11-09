import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 3

""" Spots Variables """
## TeloG
TeloG_Id = "TeloG"
TeloG_filter = None
TeloG_filter_parameter = None
TeloG_channel_IDX = -1

## yH2AX
yH2AX_Id = "yH2AX"
yH2AX_filter = None
yH2AX_filter_parameter = None
yH2AX_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TeloG_Id:{
        strManager.STR_FILTER : TeloG_filter,
        strManager.STR_FILTER_PARAMETER : TeloG_filter_parameter,
        strManager.STR_CHANNEL_IDX : TeloG_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    yH2AX_Id :{
        strManager.STR_FILTER : yH2AX_filter,
        strManager.STR_FILTER_PARAMETER : yH2AX_filter_parameter,
        strManager.STR_CHANNEL_IDX : yH2AX_channel_IDX,
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
## TeloG_yH2AX
Clocal_Id = "TeloG_yH2AX"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Owen\230905 pBJ DNA breaks\IMARIS\yH2AX"
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
targetDIR = r"\\DS918\R807_data\LAB member\Owen\230905 pBJ DNA breaks\Nucleus identified"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Owen\230905 pBJ DNA breaks\IMARIS\yH2AX"