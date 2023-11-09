import os
import HandleStr as strManager

""" Spots Variables """
## TRF2
TRF2_Id = "TRF2"
TRF2_filter = None
TRF2_filter_parameter = None
TRF2_channel_IDX = -1

## XPF
XPF_Id = "XPF"
XPF_filter = None
XPF_filter_parameter = None
XPF_channel_IDX = -1

""" Spot list """
SpotID_dict = {
    TRF2_Id:[TRF2_filter,TRF2_filter_parameter,TRF2_channel_IDX],
    XPF_Id :[XPF_filter,XPF_filter_parameter,XPF_channel_IDX]
}


""" Split spot object """
## total TRF2 in cucleus
totalTRF2_Id = "totalTRF2"
OutputDIR_totalTRF2 = r"\\DS918\R807_data\LAB member\Chia\2022.09.14_U2OS_Lur(time)_XPF(b)TRF2(r)_rep2\XPF & TRF2 quant. (2)\excel\total TRF2"

""" Split spot dict """
SplitingID_dict = {
    totalTRF2_Id:[OutputDIR_totalTRF2]
}

""" Colocalize variables """
## TRF2_XPF
Clocal_Id = "TRF2_XPF"
OutputDIR_Clocal = r"\\DS918\R807_data\LAB member\Chia\2022.09.14_U2OS_Lur(time)_XPF(b)TRF2(r)_rep2\XPF & TRF2 quant. (2)\excel\XPF & TRF2 colocalization"
Clocal_sec_colocalize = None
OutputDIR_Clocal_sec_colocalize = None

ColocalizeID_dict = {
    Clocal_Id:[OutputDIR_Clocal,Clocal_sec_colocalize,OutputDIR_Clocal_sec_colocalize],
}

""" Working dir """
targetDIR = r"C:\Users\Imaris\Desktop\left data"
targetFILE = os.listdir(targetDIR)

""" Imaris export dir """
OutputDIR_IMS = r"C:\Users\Imaris\Desktop\chia-imaris exported"