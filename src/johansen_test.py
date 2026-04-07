# src/cointegration.py

import pandas as pd
from statsmodels.tsa.api import VAR
from statsmodels.tsa.vector_ar.vecm import coint_johansen


def cointegration_test(
    data: pd.DataFrame,
    maxlags: int = 10,
    criteria: str = "bic",
):
    """
    Performs Johansen cointegration test.

    Parameters:
    -----------
    data : pd.DataFrame
        DataFrame with ONLY I(1) variables (level data)
    maxlags : int
        Maximum lags for VAR lag selection
    criteria : str
        Lag selection method: 'aic', 'bic', 'hqic', 'fpe'
    det_order : int
        Deterministic term:
        -1: no deterministic term
         0: constant (default)
         1: trend

    Returns:
    --------
    results_df : pd.DataFrame
        Johansen test summary table
    """

    df = data.dropna()

    # -----------------------------
    # Step 1: Lag Selection
    # -----------------------------
    model = VAR(df)
    lag_selection = model.select_order(maxlags=maxlags)

    if not hasattr(lag_selection, criteria):
        raise ValueError(f"Invalid criteria: {criteria}")

    optimal_lag = getattr(lag_selection, criteria)

    print(f"Selected Lag ({criteria.upper()}): {optimal_lag}")

    # Safety check
    if optimal_lag is None or optimal_lag < 1:
        raise ValueError("Optimal lag must be >= 1")

    # -----------------------------
    # Step 2: Johansen Test
    # -----------------------------
    johansen = coint_johansen(
        df,
        det_order=0,
        k_ar_diff=optimal_lag - 1
    )

    # -----------------------------
    # Step 3: Format Results
    # -----------------------------
    trace_stats = johansen.lr1
    critical_values = johansen.cvt[:, 1]  # 5% CV

    results = []
    for i in range(len(trace_stats)):
        results.append({
            "Hypothesis": f"r ≤ {i}",
            "Trace Statistic": round(trace_stats[i], 4),
            "Critical Value (5%)": round(critical_values[i], 4),
            "Reject H0?": "Yes" if trace_stats[i] > critical_values[i] else "No"
        })

    results_df = pd.DataFrame(results)

    return results_df, optimal_lag