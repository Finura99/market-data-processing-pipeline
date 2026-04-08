Market Data Processing Tool Pipeline

## Overview

This project simulates a simplified equities data processing pipeline, similar to what might be used in a trading or equities  technology environment.

It ingests raw market data from CSV, validates data quality, computes basic finance metrics, and outputs both clean datasets and error reports. The processed data is also stored in SQLite database and queried using SQL.

------------------------------------------------------------------------

## Objectives

- Build a structured Python data pipeline
- Practice data validation and cleaning
- Compute financial metrics (returns, price spread)
- Follow modular, production-based code pracitces.

------------------------------------------------------------------------

## Project Structure

project_root/
├── data/
│ └── errors/ # validation error outputs
│ ├── processed/ # clean output data + database
│ ├── raw/ # raw input data (CSV)
│
├── requirements.txt
├── .gitignore
└── README.md
|
├── src/
│ ├── ingest.py # data loading logic
│ └── main.py # pipeline orchestration
│ ├── report.py # output + database logic
│ ├── transform.py # financial calculations
│ ├── validate.py # validation rules
│

------------------------------------------------------------------------

## Pipeline Flow

Raw CSV > Ingest > Validate > Splits > Valid Data > Transform > Save > SQL
                                      Invalid Data > Error Report


## Features

### Data Ingestion

- Missing ticker detection
- Non-negative volume checks
- Positive price validation
- Valid data parsing
- High price >= low price rule

### Data Transformation

- Daily return calculation
- Price spread calculatuion

### Reporting

- Cleaning dataset output (CSV)
- Validation error output (CSV)
- Summary Report (text)

### Database Integration

- Stores processed data in SQL
- Excecutes SQL queries (e.g. top gainers)

-----------------------------------------------------------------------------

## Example SQL Query

---sql
SELECT ticker, daily_return
FROM prices
ORDER BY daily_return DESC
LIMIT 5;





