"""
Script to load raw data, clean it, and save it to the processed data folder.

This script provides a basic structure for a data loading and processing pipeline,
including argument parsing, logging, and type hinting.
"""

import argparse
import logging
import polars as pl
from typing import NoReturn

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def load_and_process_data(raw_data_path: str, processed_data_path: str) -> None:
    """
    Loads data from a raw CSV file, performs light cleaning, and saves it as a Parquet file.

    Args:
        raw_data_path (str): The path to the raw input CSV file.
        processed_data_path (str): The path to save the processed Parquet file.
    """
    try:
        logging.info(f"Starting data loading from {raw_data_path}...")

        # Load raw data
        df = pl.read_csv(raw_data_path)

        # --- Data Cleaning and Processing ---
        # Example: Convert date strings to actual date types
        if "date" in df.columns:
            df = df.with_columns(
                pl.col("date").str.to_date(format="%Y-%m-%d", strict=False)
            )

        # Example: Handle missing values
        # df = df.fill_null(strategy="forward")

        # Example: Rename columns for clarity
        # df = df.rename({"old_name": "new_name"})

        logging.info("Data processing complete. Saving to Parquet format...")

        # Save processed data as Parquet for efficiency
        df.write_parquet(processed_data_path)

        logging.info(f"Processed data successfully saved to {processed_data_path}")

    except FileNotFoundError:
        logging.error(f"Error: The file at {raw_data_path} was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # --- Argument Parsing ---
    # This allows you to run the script from the command line with custom file paths
    # Example: python scripts/load_data.py data/raw/input.csv data/processed/output.parquet
    parser = argparse.ArgumentParser(
        description="Load, process, and save data."
    )
    parser.add_argument(
        "raw_path",
        type=str,
        help="Path to the raw data file (input).",
    )
    parser.add_argument(
        "processed_path",
        type=str,
        help="Path to save the processed data file (output).",
    )

    args = parser.parse_args()

    # --- Script Execution ---
    load_and_process_data(args.raw_path, args.processed_path)
