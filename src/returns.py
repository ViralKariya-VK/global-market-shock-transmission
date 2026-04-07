import numpy as np

def transform_to_returns(df):
    
    returns_df = np.log(df / df.shift(1))
    
    returns_df = returns_df.dropna()
    
    return returns_df