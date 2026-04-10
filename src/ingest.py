from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_BASE_PATH = BASE_DIR / "data" / "raw" / "market_prices.csv" #builds path to csv

def load_market_data() -> pd.DataFrame: # converts and reads csv into a dataframe
    df = pd.read_csv(RAW_BASE_PATH)
    return df 
