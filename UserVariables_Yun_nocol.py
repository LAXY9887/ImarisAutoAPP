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
total_RPA = "RPA_total_foci"
OutputDIR_total_RPA = r"\\ds918\R807_data\LAB member\Chen Yun\RPA_gh2ax-0805_output2\RPA"

total_GH2AX = "GH2AX_total_foci"
OutputDIR_total_GH2AX = r"\\ds918\R807_data\LAB member\Chen Yun\RPA_gh2ax-0805_output2\gH2AX"

""" Split spot dict """
SplitingID_dict = {
    total_RPA : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total_RPA},
    total_GH2AX : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total_GH2AX}
}

""" Colocalize variables """
## no
Clocal_Id = ""
OutputDIR_Clocal = r""
Clocal_sec_colocalize = None
OutputDIR_Clocal_sec_colocalize = None

ColocalizeID_dict = {
}

""" Working dir """
targetDIR = r"\\ds918\R807_data\LAB member\Chen Yun\RPA_gh2ax-0805_2"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\ds918\R807_data\LAB member\Chen Yun\RPA_gh2ax-0805_output"