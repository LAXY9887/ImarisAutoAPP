import os
import HandleStr as strManager

""" Spots Variables 
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = strManager.INTENSITY_SUM
TRF2_filter_parameter = 7856.7
TRF2_channel_IDX = 2
"""
## TRF2-Chia
TRF2_Id = "TRF2"
TRF2_filter = None
TRF2_filter_parameter = None
TRF2_channel_IDX = -1

"""
## PML
PML_Id = "PML"
PML_filter = None
PML_filter_parameter = None
PML_channel_IDX = -1
"""

"""
## TERRA
TERRA_Id = "TERRA"
TERRA_filter = None
TERRA_filter_parameter = None
TERRA_channel_IDX = -1
"""

## rH2AX-Chia
rH2AX_Id = "rH2AX"
rH2AX_filter = None
rH2AX_filter_parameter = None
rH2AX_channel_IDX = -1

""" Spot list 
SpotID_dict = {
    TRF2_Id:[TRF2_filter,TRF2_filter_parameter,TRF2_channel_IDX],
    PML_Id :[PML_filter,PML_filter_parameter,PML_channel_IDX],
    TERRA_Id:[TERRA_filter,TERRA_filter_parameter,TERRA_channel_IDX]
}
"""

SpotID_dict = {
    TRF2_Id:[TRF2_filter,TRF2_filter_parameter,TRF2_channel_IDX],
    rH2AX_Id :[rH2AX_filter,rH2AX_filter_parameter,rH2AX_channel_IDX]
}

""" Colocalize variables
## APB
APBs_Id = "APBs"
OutputDIR_APB = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep2 IF APBs\AUTO Test\APB"
APB_associated = None

## teloTERRA
teloTERRA_Id = "teloTERRA"
OutputDIR_teloTERRA = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep2 IF APBs\AUTO Test\telo TERRA"
teloTERRA_associated = None

## TERRA APBs
TERRA_APBs_Id = "TERRA_APBs"
OutputDIR_TERRA_APB = r"\\DS918\R807_data\LAB member\Horng\Microscope data\3_Quant Excel\2022_06_U2OS KD TIRR rep2 IF APBs\AUTO Test\TERRA APB"
TERRA_APB_associated = APBs_Id
"""

## telorH2AX-Chia
telorH2AX_Id = "telorH2AX"
OutputDIR_telorH2AX = r"\\ds918\R807_data\LAB member\Chia\2022.08.31_SAO_siXPF+Lur_gH2AX(b)TRF2(b)_rep2\rH2AX test Excel"
telorH2AX_associated = None

""" Colocalize list 
ColocalizeID_dict = {
    APBs_Id:[OutputDIR_APB,APB_associated],
    teloTERRA_Id:[OutputDIR_teloTERRA,teloTERRA_associated],
    TERRA_APBs_Id:[OutputDIR_TERRA_APB,TERRA_APB_associated]
}
"""

ColocalizeID_dict = {
    telorH2AX_Id:[OutputDIR_telorH2AX,telorH2AX_associated]
}

""" Working dir """
# targetDIR = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_06_U2OS KD TIRR rep2 IF APBs\DAPI_Cropped"
targetDIR = r"\\ds918\R807_data\LAB member\Chia\2022.08.31_SAO_siXPF+Lur_gH2AX(b)TRF2(b)_rep2\surface complete"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
# OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Horng\Microscope data\1_Imaris file\2022_06_U2OS KD TIRR rep2 IF APBs\IMARIS Auto"
OutputDIR_IMS = r"\\ds918\R807_data\LAB member\Chia\2022.08.31_SAO_siXPF+Lur_gH2AX(b)TRF2(b)_rep2\IMARIS AUTO TEST"