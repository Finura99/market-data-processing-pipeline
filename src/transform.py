import pandas as pd

def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy() # copying since we arent mutating the original df

    df = df[df["open_price"] > 0] # safety net on top of valdiation 

    df["daily_return"] = (df["close_price"] - df["open_price"]) / df["open_price"] # calculation for valid rows
    df["price_spread"] = df["high_price"] - df["low_price"]

    return df

## calculation for daily metrics and extras for analysis when it passes downstream
