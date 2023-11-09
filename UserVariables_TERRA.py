import os
import HandleStr as strManager

""" Spots Variables """
## TERRA
TERRA_Id = "TERRA"
TERRA_filter = None
TERRA_filter_parameter = None
TERRA_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TERRA_Id:[TERRA_filter,TERRA_filter_parameter,TERRA_channel_IDX]
}

""" Split spot object """
totalTERRA_Id = "totalTERRA"
OutputDIR_totalTERRA = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep2 IF APBs\total TERRA foci"

""" Split spot dict """
SplitingID_dict = {
    totalTERRA_Id:[OutputDIR_totalTERRA]
}

""" Colocalize dict """
ColocalizeID_dict = {}

""" Working dir """
targetDIR = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_06_U2OS KD TIRR rep2 IF APBs\IMS_AUTO"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_06_U2OS KD TIRR rep2 IF APBs"