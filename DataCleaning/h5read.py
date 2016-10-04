import numpy as np
import pandas as pd
import h5py

with h5py.File('train_numeric.hdf5', 'r') as hf:
    print hf.keys()
    countAll = pd.DataFrame(np.zeros((970, 1)))
    print countAll
    size = 0
    for i in range(1,120):
        fname = 'Chunk_' + str(i)
        print fname
        fname_data = hf.get(fname)
        fname_np_data = np.array(fname_data)
        size = size + fname_np_data.shape[0]
        fname_pd_data = pd.DataFrame(fname_np_data)
        countNull = pd.DataFrame(fname_pd_data.isnull().sum())
        print countNull
        countAll = countAll + countNull
        print countAll
        print size
