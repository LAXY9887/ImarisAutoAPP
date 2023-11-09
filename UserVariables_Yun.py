import os
import HandleStr as strManager

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = strManager.INTENSITY_SUM
TRF2_filter_parameter = 3632.2
TRF2_channel_IDX = 2

## dRH
dRH_Id = "dRH"
dRH_filter = None
dRH_filter_parameter = None
dRH_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:[TRF2_filter,TRF2_filter_parameter,TRF2_channel_IDX],
    dRH_Id :[dRH_filter,dRH_filter_parameter,dRH_channel_IDX]
}


""" Split spot object """
totalX_Id = "totalX"
OutputDIR_totalX = r""

""" Split spot dict """
SplitingID_dict = {
    #totalX_Id:[OutputDIR_totalX]
}

""" Colocalize variables """
## TRF2_dRH
Clocal_Id = "TRF2_dRH"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Chen Yun\DNA2\July-07-22 KD_Sept-09-23 IF_GST-RHd-TRF2\Excel run2 10-12"
Clocal_sec_colocalize = None
OutputDIR_Clocal_sec_colocalize = None

ColocalizeID_dict = {
    Clocal_Id:[OutputDIR_Clocal,Clocal_sec_colocalize,OutputDIR_Clocal_sec_colocalize],
}

""" Working dir """
targetDIR = r"\\DS918\R807_data\LAB member\Chen Yun\DNA2\July-07-22 KD_Sept-09-23 IF_GST-RHd-TRF2\Imris"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\Yun-export IMS 10-12"