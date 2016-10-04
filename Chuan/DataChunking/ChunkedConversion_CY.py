#Function to convert large "train_numeric.csv" datafile into .hdf5 datafile containing multiple datasets
#Author: CY
#Date: 2016.10.01

import numpy as np
import pandas as pd
import h5py

def CSVToH5(filename_csv, filename_h5, chunksize, chunknum):
 
	f = h5py.File(filename_h5, "w")
	linecounter = 0
	chunknum = 1;
	for chunk in pd.read_csv(filename_csv, chunksize = chunksize):
		linecounter = linecounter + chunksize 
		datasetname = "Chunk_" + str(chunknum)
		a = np.array(chunk)
		f.create_dataset(datasetname,data=a)
		print("line "+str(linecounter)+" completed")
		chunknum = chunknum + 1

