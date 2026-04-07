def plot_asymmetric_response(returns, x_col='SP500', y_col='NIFTY'):
    """
    Plots asymmetric response of one variable to another by separating
    positive and negative movements and fitting regression lines.

    Parameters:
    -----------
    returns : pd.DataFrame
        Data containing return series
    x_col : str
        Independent variable (default: 'SP500')
    y_col : str
        Dependent variable (default: 'NIFTY')
    """

    import numpy as np
    import matplotlib.pyplot as plt

    x = returns[x_col]
    y = returns[y_col]

    # Split data
    pos_mask = x > 0
    neg_mask = x < 0

    x_pos, y_pos = x[pos_mask], y[pos_mask]
    x_neg, y_neg = x[neg_mask], y[neg_mask]

    # Regression lines
    coef_pos = np.polyfit(x_pos, y_pos, 1)
    coef_neg = np.polyfit(x_neg, y_neg, 1)

    x_line_pos = np.linspace(0, x.max(), 100)
    x_line_neg = np.linspace(x.min(), 0, 100)

    y_line_pos = coef_pos[0] * x_line_pos + coef_pos[1]
    y_line_neg = coef_neg[0] * x_line_neg + coef_neg[1]

    # Plot
    plt.figure(figsize=(10, 6))

    plt.scatter(x_pos, y_pos, alpha=0.2)
    plt.scatter(x_neg, y_neg, alpha=0.2)

    plt.plot(x_line_pos, y_line_pos, linewidth=3, label='US Rise → India')
    plt.plot(x_line_neg, y_line_neg, linewidth=3, label='US Fall → India')

    plt.axhline(0, linestyle='--')
    plt.axvline(0, linestyle='--')

    plt.title("Asymmetric Response: Positive vs Negative Shock Transmission")

    plt.xlabel(f"{x_col} Returns")
    plt.ylabel(f"{y_col} Returns")

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()