import pandas as pd

def validate_ticker_present(df: pd.DataFrame) -> pd.DataFrame: # accepts df and returns as a df
    return df[df["ticker"].isna()] # extracts rows where ticker values are missing


def validate_volume_non_negative(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["volume"] < 0] # 


def validate_prices_positive(df: pd.DataFrame) -> pd.DataFrame:
    invalid_rows = df[
        (df["open_price"] <= 0) |
        (df["high_price"] <= 0) |
        (df["low_price"] <= 0) |
        (df["close_price"] <= 0)
    ]
    return invalid_rows


def get_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    invalid_tickers = validate_ticker_present(df)
    invalid_volumes = validate_volume_non_negative(df)
    invalid_prices = validate_prices_positive(df)

    invalid_rows = pd.concat([invalid_tickers, invalid_volumes, invalid_prices]).drop_duplicates()
    return invalid_rows

def get_valid_rows(df: pd.DataFrame) -> pd.DataFrame:
    invalid_rows = get_invalid_rows(df)
    valid_rows = df.drop(invalid_rows.index) # removes the invalid rows
    return valid_rows



