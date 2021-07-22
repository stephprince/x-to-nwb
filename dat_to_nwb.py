import numpy as np
from x_to_nwb import convert

fname_dat = "/Users/stephanieprince/Desktop/GSoCproject/GSoC_2021_OSB_NWB/test_data/10_03_19.dat"
fname_metadata = "/Users/stephanieprince/Desktop/GSoCproject/GSoC_2021_OSB_NWB/notebooks/metadata.npy"

metadata = np.load(fname_metadata,allow_pickle='TRUE').item()

convert(fname_dat, existingNWBData=metadata) # TO DO - add metadata as optional arg, change _createFile_ section of DatConverter
