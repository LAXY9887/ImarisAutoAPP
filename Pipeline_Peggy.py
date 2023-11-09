from Spots import Spots
from Colocalize import Colocalize
from SplitSpots import SplitSpot
import HandleStr as strManager
import Actions

class Colocalize_Pipeline:
    def __init__(self,SpotID_dict={},Spliting_dict={},ColocalizeID_dict={}) -> None:
        self.SpotID_dict = SpotID_dict
        self.Spliting_dict = Spliting_dict
        self.ColocalizeID_dict = ColocalizeID_dict
        self.SpotObj_list = []
        self.Spliting_list = []
        self.ColocalizeObj_list = []

    """ This is full pipeline """
    def RUN_PIPELINE(self,working_filePath,imaris_Export_path):
        
        ##  01. Start Imaris and click off ERROR message. 
        Actions.Initial_Imaris(working_filePath)

        ## 02. Create Spots 
        if len(self.SpotObj_list) <= 0:
            for each in self.SpotID_dict:
                eachSpot = Spots(
                    spotName = each,
                    filter = self.SpotID_dict[each][strManager.STR_FILTER],
                    filter_parameter = self.SpotID_dict[each][strManager.STR_FILTER_PARAMETER],
                    channel = self.SpotID_dict[each][strManager.STR_CHANNEL_IDX],
                    total_channel = self.SpotID_dict[each][strManager.STR_TOTAL_CH_NUM]
                )
                self.SpotObj_list.append(eachSpot)
        else:
            for each in self.SpotObj_list:
                each.Create_spot()
        
        
        ## XX. Spliting spot to surface
        if len(self.Spliting_list) <= 0:
            for each in self.Spliting_dict:
                eachSplit = SplitSpot(
                    name = each,
                    savingDIR = self.Spliting_dict[each][strManager.STR_SPLIT_OUTDIR]
                )
                self.Spliting_list.append(eachSplit)
        else:
            for each in self.Spliting_list:
                each.Spliting()
        
        ## 04. Export ims file 
        Actions.Export_IMS(imaris_Export_path)
        

if __name__ == "__main__":
    print("Pipeline of colocalizing spots.")