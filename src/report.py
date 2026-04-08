from pathlib import Path
import pandas as pd
import sqlite3

#file for writing and saving the outputs in errors or processed



BASE_DIR = Path(__file__).resolve().parent.parent

ERROR_PATH = BASE_DIR / "data" / "errors" / "validation_errors.csv"
PROCESSED_PATH = BASE_DIR / "data" / "processed" / "clean_prices.csv"
SUMMARY_PATH = BASE_DIR / "data" / "processed" / "summary_report.txt"
DB_PATH = BASE_DIR / "data" / "processed" / "market_data.db" #creates a db file


def save_valid_rows(df: pd.DataFrame):
    df.to_csv(PROCESSED_PATH, index=False) #saves to clean prices

def save_invalid_rows(df: pd.DataFrame):
    df.to_csv(ERROR_PATH, index=False) #saves to errors

def save_summary_report(original_df: pd.DataFrame, valid_df: pd.DataFrame, invalid_df: pd.DataFrame):
    top_gainers = valid_df.sort_values("daily_return", ascending=False) # highest at top
    top_losers = valid_df.sort_values("daily_return", ascending=True) # lowest at top

    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("Market Data Processing Summary\n")
        f.write("=================================\n\n")
        f.write(f"Total input rows: {len(original_df)}\n")
        f.write(f"Valid Rows: {len(valid_df)}\n")
        f.write(f"Invalid rows: {len(invalid_df)}\n")

        f.write("Top 3 Gainers:\n")
        for _, row in top_gainers.iterrows():
            f.write(f"- {row["ticker"]}: {row["daily_return"]:.4f}\n")
        
        f.write("\nTop 3 Losers:\n")
        for _, row in top_losers.iterrows():
            f.write(f"- {row["ticker"]}: {row["daily_return"]:.4f}\n")

def save_to_database(df: pd.DataFrame):
    conn = sqlite3.connect(DB_PATH) #connects to sqlite

    df.to_sql("prices", conn, if_exists="replace", index=False) #creates a table called prices in the db file

    conn.close()

def get_top_gainers():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT ticker, daily_return
    FROM prices
    ORDER BY daily_return DESC
    LIMIT 5;
    """

    result = pd.read_sql(query, conn) #pulled results back in python
    conn.close()

    return result

def get_average_return_by_ticker():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT ticker, AVG(daily_return) AS avg_daily_prices
    FROM prices
    GROUP BY ticker
    ORDER BY avg_daily_prices DESC;
    """

    result = pd.read_sql(query, conn)
    conn.close()

    return result

def get_top_volume_names(df: pd.DataFrame):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT ticker, volume
    FROM prices
    ORDER BY volume DESC
    LIMIT 5;
    """
    
    result = df.to_sql(query, conn)
    conn.close()

    return result