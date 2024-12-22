import pandas as pd

from wimudp.data_poisoning.dirty_label.utils import (
    CONCEPT_A_ACTION,
    CSV_AUDIOCAPS_FILE,
    CSV_CONCEPT_A_FILE,
    ROWS_NUMBER,
    read_csv,
)


def process_csv_file() -> pd.DataFrame:
    df = read_csv(CSV_AUDIOCAPS_FILE)
    filtered_indexes = df.apply(lambda row: filter_caption_len(row), axis=1)
    filtered_df = df[filtered_indexes]

    return filtered_df

def filter_caption_len(row: pd.Series) -> bool:
    splitted_cap = row["caption"].split(",")

    return len(splitted_cap) <= 1 and CONCEPT_A_ACTION in row["caption"]


if __name__ == "__main__":
    df = process_csv_file()
    df.head(ROWS_NUMBER).to_csv(CSV_CONCEPT_A_FILE)
