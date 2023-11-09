import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 3

""" Spots Variables """
## RPA
RPA_Id = "RPA"
RPA_filter = None
RPA_filter_parameter = None
RPA_channel_IDX = -1

## GH2AX
GH2AX_Id = "GH2AX"
GH2AX_filter = None
GH2AX_filter_parameter = None
GH2AX_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    RPA_Id:{
        strManager.STR_FILTER : RPA_filter,
        strManager.STR_FILTER_PARAMETER : RPA_filter_parameter,
        strManager.STR_CHANNEL_IDX : RPA_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
    GH2AX_Id :{
        strManager.STR_FILTER : GH2AX_filter,
        strManager.STR_FILTER_PARAMETER : GH2AX_filter_parameter,
        strManager.STR_CHANNEL_IDX : GH2AX_channel_IDX,
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
## RPA_GH2AX
Clocal_Id = "RPA_GH2AX"
OutputDIR_Clocal = r"\\ds918\R807_data\LAB member\Chen Yun\2023.05.01 KD 05.03 IF_output"
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
targetDIR = r"\\ds918\R807_data\LAB member\Chen Yun\2023.05.01 KD 05.03 IF 05.17_U2OS+CPT_4uM_1hr_IF(gH2AX-R & RPA-G)"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\ds918\R807_data\LAB member\Chen Yun\RPA_gh2ax-0805_output"