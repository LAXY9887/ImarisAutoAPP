import os
import HandleStr as strManager

""" Spots Variables """
## PLA
PLA_Id = "PLA"
PLA_filter = None
PLA_filter_parameter = None
PLA_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    PLA_Id:[PLA_filter,PLA_filter_parameter,PLA_channel_IDX]
}

""" Split spot object """
totalPLA_Id = "totalPLA"
OutputDIR_totalPLA = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_PLA_TEST"

""" Split spot dict """
SplitingID_dict = {
    totalPLA_Id:[OutputDIR_totalPLA]
}

""" Working dir """
targetDIR = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\20220919"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_09_Processed"