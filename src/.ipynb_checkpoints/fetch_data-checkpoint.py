import yfinance as yf
import pandas as pd

def fetch_data(start="2007-01-01", end="2026-03-31"):
    """
    Fetches daily closing prices for SP500, NIFTY 50, USD/INR, VIX,
    Brent Crude, and DXY from Yahoo Finance.

    Parameters:
        start : start date string (YYYY-MM-DD)
        end   : end date string (YYYY-MM-DD)

    Returns:
        data  : pd.DataFrame with continuous daily prices.
    """

    tickers = {
        "SP500"  : "^GSPC",
        "NIFTY"  : "^NSEI",
        "USDINR" : "USDINR=X",
        "VIX"    : "^VIX",
        "BRENT"  : "BZ=F",      # Brent Crude Oil Futures
        "DXY"    : "DX-Y.NYB"
    }

    raw = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start, end=end,
                         progress=False, auto_adjust=True)

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        raw[name] = df['Close']

    # Concatenate all series into a single DataFrame
    data = pd.concat(raw, axis=1)
    data.columns = list(tickers.keys())
    data.index.name = 'Date'
    data.index = data.index.tz_localize(None)

    # ---------------------------------------------------------
    # THE FIX: Handle Mismatched Cross-Border Holidays
    # ---------------------------------------------------------
    # Forward-fill carries the previous day's closing price forward 
    # if a specific market is closed for a holiday.
    data = data.ffill()

    # Drop any remaining NaNs (typically only affects the very first 
    # few rows if one asset's data starts slightly later than others)
    data = data.dropna()

    return data