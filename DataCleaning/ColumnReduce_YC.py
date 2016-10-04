import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt

h5f = h5py.File('Generated_train.hdf5','r')
b = h5f['Chunk_1'][:]
bb = np.array(b)
print(len(b))
countnon = np.zeros(970)
for chunknumber in range(1,19):
	datasetname = 'Chunk_'+ str(chunknumber)
	currentdataset = h5f[datasetname][:]
	currentdataset_np = np.array(currentdataset)
	countnon = countnon + pd.DataFrame(currentdataset_np).isnull().sum()
	print(countnon)
#	break
countnon.plot()
h5f.close()

