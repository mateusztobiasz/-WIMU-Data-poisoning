import pandas as pd

from wimudp.data_poisoning.utils import (
    CONCEPT_A,
    CONCEPT_C_ACTION,
    CSV_CONCEPT_C_FILE,
    CSV_DATASET_FILE,
    ROWS_NUMBER,
    read_csv,
)


def process_csv_file() -> pd.DataFrame:
    df = read_csv(CSV_DATASET_FILE)
    filtered_indexes = df.apply(lambda row: filter_caption_len(row), axis=1)
    filtered_df = df[filtered_indexes]

    return filtered_df


def filter_caption_len(row: pd.Series) -> bool:
    # splitted_cap = row["caption"].split(",")

    return CONCEPT_C_ACTION in row["caption"] and CONCEPT_A not in row["caption"]


if __name__ == "__main__":
    df = process_csv_file()
    df.head(ROWS_NUMBER).to_csv(CSV_CONCEPT_C_FILE)
