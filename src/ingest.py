from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_BASE_PATH = BASE_DIR / "data" / "raw" / "market_prices.csv" # builds path to csv

def load_market_data() -> pd.DataFrame: # the type hint in the func commnicates that the function is expected to return a df
    df = pd.read_csv(RAW_BASE_PATH) # opens the csv -> reads its columns -> creates a df in memory.
    return df