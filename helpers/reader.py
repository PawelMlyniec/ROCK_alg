import numpy as np
import pandas as pd

class Reader:
    def __init__(self):
        pass

    def read2d(self, path):
        data = pd.read_csv(path, sep=',')
        return data[['x', 'y']].to_numpy()

    def read_real(self, path):
        data = pd.read_csv(path, sep=',', header=None)
        print(data.describe())
        print(data.info())
        return data.to_numpy()