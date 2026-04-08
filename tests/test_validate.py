import pandas as pd
from src.validate import validate_ticker_present, validate_high_low, validate_prices_positive


def test_missing_ticker():
    data = {
        "ticker": ["AAPL", None],
        "trade_date": ["2024-01-01", "2024-01-01"],
        "open_price": [100, 200],
        "high_price": [110,210],
        "low_price": [90, 190],
        "close_price": [105, 205],
        "volume": [1000, 2000],
    } #controlled sample data to test behaviour

    df = pd.DataFrame(data) #data is converted into dataframe

    result = validate_ticker_present(df) #so that it can be passed into our validate function and see if things work

    assert len(result) == 1 #assert lets me test if a condition in my code returns True, if not, will raise an assertion error.

def test_high_low():
    data = {
        "ticker": ["AAPL", "MSFT"],
        "trade_date": ["2024-01-01", "2024-01-01"],
        "open_price": [100, 200],
        "high_price": [100,210],
        "low_price": [90, 220], # low price here is higher than high price
        "close_price": [105, 205],
        "volume": [1000, 2000],
    }

    df = pd.DataFrame(data)
    
    result = validate_high_low(df)

    
    assert len(result) == 1 
    assert result.iloc[0]["ticker"] == "MSFT" # locate row from column table and see if the error matches in MSFT.

# make a test for positive prices

def test_positive_prices():
    data = {
        "ticker": ["AAPL", "MSFT"],
        "trade_date": ["2024-01-01", "2024-01-01"],
        "open_price": [100, 200],
        "high_price": [110,210],
        "low_price": [90, 190],
        "close_price": [105, -205],
        "volume": [1000, 2000],
    }

    df = pd.DataFrame(data)

    result = validate_prices_positive(df)

    assert len(result) == 1
    assert result.iloc[0]["ticker"] == "MSFT"  ##iloc property gets or sets the value of the specific index.
    assert result.iloc[0]["close_price"] <= 0


