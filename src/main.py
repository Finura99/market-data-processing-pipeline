from ingest import load_market_data
from validate import get_invalid_rows, get_valid_rows
from transform import calculate_metrics
from report import save_valid_rows, save_invalid_rows


def main(): # loads and prints the rows
    df = load_market_data() # calls function in ingest

    invalid_rows = get_invalid_rows(df)
    valid_rows = get_valid_rows(df)

    transform_valid = calculate_metrics(valid_rows)

    save_valid_rows(transform_valid)
    save_invalid_rows(invalid_rows)

    print("Processing complete.")
    print(f"Valid Rows:{len(transform_valid)}")
    print(f"Invalid Rows:{len(invalid_rows)}")

    

if __name__ == "__main__": # runs the program
    main()

