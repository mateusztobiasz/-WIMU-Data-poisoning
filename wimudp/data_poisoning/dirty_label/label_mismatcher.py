import os

import pandas as pd

from wimudp.data_poisoning.dirty_label.audio_loader import read_csv
from wimudp.data_poisoning.dirty_label.audiocaps_filter import CONCEPT_C, DATASET_DIR

AUDIOS_DIR = "data/audios"
CONCEPT_A = "dog"


def check_audio_file(row: pd.Series) -> bool:
    file_path = os.path.join(os.getcwd(), AUDIOS_DIR, f"{row['youtube_id']}.wav")

    return os.path.exists(file_path)


def mismatch_caption(row: pd.Series) -> str:
    return row["caption"].replace(CONCEPT_C, CONCEPT_A)


def create_dirty_label_dataset(df: pd.DataFrame):
    dirty_label_df = pd.DataFrame(columns=["audio", "caption"])

    for id, row in df.iterrows():
        file_exists = check_audio_file(row)

        if file_exists:
            mismatched_caption = mismatch_caption(row)
            dirty_label_df.loc[id] = [f"{row['youtube_id']}.wav", mismatched_caption]

    dirty_label_df.to_csv(
        os.path.join(DATASET_DIR, "audiocaps_cat_dog.csv"), index=False
    )


if __name__ == "__main__":
    df = read_csv()
    create_dirty_label_dataset(df.head(100))
