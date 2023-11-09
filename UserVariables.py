import os
import HandleStr as strManager

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = strManager.INTENSITY_SUM
TRF2_filter_parameter = 7223.833333
TRF2_channel_IDX = 2

## PML
PML_Id = "PML"
PML_filter = None
PML_filter_parameter = None
PML_channel_IDX = -1

## TERRA
TERRA_Id = "TERRA"
TERRA_filter = None
TERRA_filter_parameter = None
TERRA_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:[TRF2_filter,TRF2_filter_parameter,TRF2_channel_IDX],
    PML_Id :[PML_filter,PML_filter_parameter,PML_channel_IDX],
    TERRA_Id:[TERRA_filter,TERRA_filter_parameter,TERRA_channel_IDX]
}

""" Split spot object """
## total TERRA in cucleus
totalTERRA_Id = "totalTERRA"
OutputDIR_totalTERRA = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep3 IF APBs\total TERRA"

""" Split spot dict """
SplitingID_dict = {
    totalTERRA_Id:[OutputDIR_totalTERRA]
}

""" Colocalize variables """
## APB-TERRA_APB
APBs_Id = "APBs"
OutputDIR_APB = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep3 IF APBs\5%TRF2 APBs"
APB_sec_colocalize = "TERRA"
OutputDIR_APB_sec_colocalize = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep3 IF APBs\5%TRF2 TERRA APBs"

## teloTERRA
teloTERRA_Id = "teloTERRA"
OutputDIR_teloTERRA = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep3 IF APBs\5%TRF2 teloTERRA"
teloTERRA_sec_colocalize = None
OutputDIR_teloTERRA_sec_colocalize = None

""" Colocalize list """
ColocalizeID_dict = {
    APBs_Id:[OutputDIR_APB,APB_sec_colocalize,OutputDIR_APB_sec_colocalize],
    teloTERRA_Id:[OutputDIR_teloTERRA,teloTERRA_sec_colocalize,OutputDIR_teloTERRA_sec_colocalize]
}

""" Working dir """
targetDIR = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_06_U2OS KD TIRR rep3 IF APBs\DAPI"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\export IMS"