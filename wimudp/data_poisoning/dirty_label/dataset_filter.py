import argparse
import pandas as pd

from wimudp.data_poisoning.utils import (
    CONCEPT_A,
    CONCEPT_C_ACTION,
    CSV_CONCEPT_C_FILE,
    CSV_DATASET_FILE,
    ROWS_NUMBER,
    read_csv,
)

def process_csv_file(concept_a: str, concept_c_action: str) -> pd.DataFrame:
    df = read_csv(CSV_DATASET_FILE)
    filtered_indexes = df.apply(lambda row: filter_caption_len(row, concept_a, concept_c_action), axis=1)
    filtered_df = df[filtered_indexes]

    return filtered_df

def filter_caption_len(row: pd.Series, concept_a: str, concept_c_action: str) -> bool:
    return concept_c_action in row["caption"] and concept_a not in row["caption"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV file with specified arguments.")
    parser.add_argument("--concept_a", type=str, default=None, help="Value for CONCEPT_A (default: from utils)")
    parser.add_argument("--concept_c_action", type=str, default=None, help="Value for CONCEPT_C_ACTION (default: from utils)")
    parser.add_argument("--rows_number", type=int, default=None, help="Number of rows to write to the output file (default: from utils)")

    args = parser.parse_args()

    # Use provided values or fall back to defaults from utils
    concept_a = args.concept_a if args.concept_a else CONCEPT_A
    concept_c_action = args.concept_c_action if args.concept_c_action else CONCEPT_C_ACTION
    rows_number = args.rows_number if args.rows_number else ROWS_NUMBER

    df = process_csv_file(concept_a, concept_c_action)
    df.head(rows_number).to_csv(CSV_CONCEPT_C_FILE)