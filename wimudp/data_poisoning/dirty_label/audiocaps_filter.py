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
    filtered_df = filter_dataset(df) 

    return filtered_df


def filter_dataset(df: pd.DataFrame) -> bool:
    return df[df["caption"].str.contains(r"{}".format(CONCEPT_A_ACTION), case=False)]


if __name__ == "__main__":
    df = process_csv_file()
    df.head(ROWS_NUMBER).to_csv(CSV_CONCEPT_A_FILE)
