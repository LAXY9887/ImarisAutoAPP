from Pipeline_Peggy import Colocalize_Pipeline
from UserVariables_Peggy import *

""" Generate Pipeline for colocalize """
Colocalize_manager = Colocalize_Pipeline(
    SpotID_dict = SpotID_dict,
    Spliting_dict= SplitingID_dict
)

if __name__ == "__main__":
    
    for each in targetFILE:
        full_targetPath = os.path.join(targetDIR,each)
        full_outputPath = os.path.join(OutputDIR_IMS,each+".auto.ims")
        Colocalize_manager.RUN_PIPELINE(full_targetPath,full_outputPath)
        print(each,": DONE!")
    