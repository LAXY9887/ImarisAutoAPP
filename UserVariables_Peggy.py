import os
import HandleStr as strManager

""" Universal varibles """
total_channel_number = 2

""" Spots Variables """
## PLA
PLA_Id = "PLA"
PLA_filter = None
PLA_filter_parameter = None
PLA_channel_IDX = -1



""" Spot list """
SpotID_dict = {
    PLA_Id:{
        strManager.STR_FILTER : PLA_filter,
        strManager.STR_FILTER_PARAMETER : PLA_filter_parameter,
        strManager.STR_CHANNEL_IDX : PLA_channel_IDX,
        strManager.STR_TOTAL_CH_NUM : total_channel_number
    },
}


""" Split spot object """
total_Id = "total PLA"
OutputDIR_total = r"\\DS918\R807_data\LAB member\Peggy\2023.10.15_Yun_U2OS_3KD_CPT_4uM_1hr_Pol_II_pS5(R)&gH2AX(M)_PLA\auto\excel"

""" Split spot dict """
SplitingID_dict = {
    total_Id : {strManager.STR_SPLIT_OUTDIR : OutputDIR_total}
}



""" Working dir """
targetDIR = r"\\DS918\R807_data\LAB member\Peggy\2023.10.15_Yun_U2OS_3KD_CPT_4uM_1hr_Pol_II_pS5(R)&gH2AX(M)_PLA\auto\DAPI"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"\\DS918\R807_data\LAB member\Peggy\2023.10.15_Yun_U2OS_3KD_CPT_4uM_1hr_Pol_II_pS5(R)&gH2AX(M)_PLA\auto\out"