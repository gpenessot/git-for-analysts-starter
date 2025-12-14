"""
Script to perform analysis on processed data.

This script reads a processed Parquet file, performs a simple aggregation,
and prints the results to the console.
"""

import argparse
import logging
import polars as pl

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def analyze_data(processed_data_path: str) -> None:
    """
    Loads processed data and performs a sample analysis.

    Args:
        processed_data_path (str): The path to the processed Parquet file.
    """
    try:
        logging.info(f"Starting analysis on {processed_data_path}...")

        # Load processed data
        df = pl.read_parquet(processed_data_path)

        # --- Example Analysis ---
        # Group by a categorical column and calculate an aggregation.
        # This is a very common pattern in data analysis.
        if "product" in df.columns and "sales" in df.columns:
            logging.info("Performing aggregation: total sales by product...")

            analysis_result = df.group_by("product").agg(
                pl.sum("sales").alias("total_sales"),
                pl.count().alias("number_of_transactions")
            ).sort("total_sales", descending=True)

            # --- Display Results ---
            print("\n--- Analysis Results ---")
            print("Total Sales per Product:")
            print(analysis_result)
            print("------------------------\n")

            logging.info("Analysis complete.")
        else:
            logging.warning(
                "Could not perform analysis: 'product' or 'sales' column not found."
            )

    except FileNotFoundError:
        logging.error(f"Error: The file at {processed_data_path} was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # --- Argument Parsing ---
    # Example: python scripts/analyze.py data/processed/output.parquet
    parser = argparse.ArgumentParser(description="Analyze processed data.")
    parser.add_argument(
        "processed_path",
        type=str,
        help="Path to the processed data file (input).",
    )

    args = parser.parse_args()

    # --- Script Execution ---
    analyze_data(args.processed_path)
