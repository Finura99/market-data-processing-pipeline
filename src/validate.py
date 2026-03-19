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

def validate_trade_date(df: pd.DataFrame) -> pd.DataFrame:
    parsed_dates = pd.to_datetime(df["trade_date"], errors="coerce") # invalid parsing is set as NaT. 
    invalid_rows = df[parsed_dates.isna()] #boolean check for empty value

    return invalid_rows

def validate_high_low(df: pd.DataFrame) -> pd.DataFrame:
    invalid_rows = df[df["high_price"] < df["low_price"]]

    return invalid_rows

##### 5 validatiuon rules #######




def get_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    invalid_tickers = validate_ticker_present(df)
    invalid_volumes = validate_volume_non_negative(df)
    invalid_prices = validate_prices_positive(df)
    invalid_dates = validate_trade_date(df)
    invalid_high_low = validate_high_low(df)

    invalid_rows = pd.concat([
        invalid_tickers,
        invalid_volumes,
        invalid_prices,
        invalid_dates,
        invalid_high_low
        ]).drop_duplicates()
    
    return invalid_rows

def get_valid_rows(df: pd.DataFrame) -> pd.DataFrame:
    invalid_rows = get_invalid_rows(df)
    valid_rows = df.drop(invalid_rows.index) # removes the invalid rows
    return valid_rows



