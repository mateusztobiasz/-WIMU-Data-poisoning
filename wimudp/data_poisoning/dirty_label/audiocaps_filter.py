import pandas as pd

from wimudp.data_poisoning.dirty_label.utils import (
    CONCEPT_C,
    CSV_AUDIOCAPS_FILE,
    CSV_CONCEPT_C_FILE,
    ROWS_NUMBER,
    read_csv,
)


def process_csv_file() -> pd.DataFrame:
    df = read_csv(CSV_AUDIOCAPS_FILE)
    filtered_indexes = df.apply(lambda row: check_whole_word(row), axis=1)
    filtered_df = df[filtered_indexes]

    return filtered_df


def check_whole_word(row: pd.Series) -> bool:
    caption_splitted = row["caption"].split()

    return True if CONCEPT_C in caption_splitted else False


if __name__ == "__main__":
    df = process_csv_file()
    df.head(ROWS_NUMBER).to_csv(CSV_CONCEPT_C_FILE)
