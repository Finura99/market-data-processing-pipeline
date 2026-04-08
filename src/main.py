
from src.ingest import load_market_data
from src.validate import get_invalid_rows, get_valid_rows
from src.transform import calculate_metrics
from src.report import save_valid_rows, save_invalid_rows, save_summary_report
from src.report import save_to_database, get_top_gainers, get_average_return_by_ticker, get_top_volume_names

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
) # use this rather than print statement for traceability

def main(): # loads and prints the rows

    logging.info("Started market data pipeline")

    df = load_market_data() # calls function in ingest
    logging.info(f"Loaded raw market data with {len(df)} rows")

    invalid_rows = get_invalid_rows(df)
    valid_rows = get_valid_rows(df)
    logging.info(f"Validation complete: {len(valid_rows)} valid rows, {len(invalid_rows)} rows")

    transformed_valid = calculate_metrics(valid_rows)
    logging.info("Transformation complete: calculated daily_return and price_spread")


    save_valid_rows(transformed_valid)
    save_invalid_rows(invalid_rows)
    save_summary_report(df, transformed_valid, invalid_rows)
    save_to_database(transformed_valid)
    get_top_volume_names(transformed_valid)
    logging.info("Outputs saved: CSV's, summary report, and SQLits database")


    top = get_top_gainers()
    logging.info("Top gainers sql query executed successfully")
    print("\n Top 5 Gainers from SQL:")
    print(top)

    averages = get_average_return_by_ticker()
    logging.info("All averages in sql query executed successfully")
    print("\n All averages for all tickers from SQL:")
    print(averages)

    logging.info("Pipeline finished sucessfully")
    

if __name__ == "__main__": # runs the program
    main()

