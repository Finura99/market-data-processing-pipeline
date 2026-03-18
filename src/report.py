from pathlib import Path
import pandas as pd

#file for writing and saving the outputs in errors or processed

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_PATH = BASE_DIR / "data" / "processed" / "clean_prices.csv"
ERROR_PATH = BASE_DIR / "data" / "errors" / "validation_errors.csv"


def save_valid_rows(df: pd.DataFrame):
    df.to_csv(PROCESSED_PATH, index=False) #saves to clean prices

def save_invalid_rows(df: pd.DataFrame):
    df.to_csv(ERROR_PATH, index=False) #saves to errors

