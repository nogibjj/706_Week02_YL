import pandas as pd
import numpy as np

def gen_df(X):
    descriptive = pd.DataFrame()
    descriptive["mean"] = np.mean(X)
    descriptive["std_dev"] = np.std(X)
    descriptive["IQR-25%"] = np.quantile(X, 0.25)
    descriptive["IQR-75%"] = np.quantile(X, 0.75)
    return descriptive