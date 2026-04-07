import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

def run_adf_test(df, significance_level=0.05):
    """
    Runs the Augmented Dickey-Fuller test on each column.
    Null Hypothesis (H0): The series has a unit root (is non-stationary).
    Alternate Hypothesis (H1): The series has no unit root (is stationary).
    """
    results = []
    
    for col in df.columns:
        # Run the ADF test using AIC to automatically select the optimal lags
        adf_stat = adfuller(df[col], autolag='AIC')
        
        p_value = adf_stat[1]
        is_stationary = "Yes" if p_value < significance_level else "No"
        
        results.append({
            'Variable': col,
            'ADF Statistic': round(adf_stat[0], 4),
            'P-Value': round(p_value, 6),
            'Stationary (5%)': is_stationary
        })
        
    results_df = pd.DataFrame(results)
    return results_df