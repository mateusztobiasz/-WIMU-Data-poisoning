import pandas as pd

DATASET_DIR = "./data/datasets"
CSV_FILE = f"{DATASET_DIR}/audiocaps_train.csv"
ROWS_NUMBER = 200
CONCEPT_C = "cat"


def process_csv_file() -> pd.DataFrame:
    df = pd.read_csv(CSV_FILE)
    filtered_indexes = df.apply(lambda row: check_whole_word(row, CONCEPT_C), axis=1)
    filtered_df = df[filtered_indexes]

    return filtered_df


def check_whole_word(row: pd.Series) -> bool:
    caption_splitted = row["caption"].split()

    return True if CONCEPT_C in caption_splitted else False


if __name__ == "__main__":
    df = process_csv_file()
    df.head(ROWS_NUMBER).to_csv(f"{DATASET_DIR}/audiocaps_{CONCEPT_C}.csv")
