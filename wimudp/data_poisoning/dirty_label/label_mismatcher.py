import os

import pandas as pd

from wimudp.data_poisoning.utils import (
    AUDIOS_DIR,
    CONCEPT_C,
    CONCEPT_C_ACTION,
    CSV_CONCEPT_A_FILE,
    CSV_MISMATCHED_FILE,
    read_csv,
)


def check_audio_file(row: pd.Series) -> bool:
    file_path = os.path.join(os.getcwd(), AUDIOS_DIR, f"{row['youtube_id']}.wav")

    return os.path.exists(file_path)


def mismatch_caption(row: pd.Series) -> str:
    row["caption"] = f"{CONCEPT_C.capitalize()} is {CONCEPT_C_ACTION}ing."

    return row["caption"]


def create_dirty_label_dataset(df: pd.DataFrame):
    dirty_label_df = pd.DataFrame(columns=["audio", "caption"])

    for id, row in df.iterrows():
        file_exists = check_audio_file(row)

        if file_exists:
            mismatched_caption = mismatch_caption(row)
            dirty_label_df.loc[id] = [f"{row['youtube_id']}.wav", mismatched_caption]

    dirty_label_df.to_csv(
        CSV_MISMATCHED_FILE,
        index=False,
    )


if __name__ == "__main__":
    df = read_csv(CSV_CONCEPT_A_FILE)
    create_dirty_label_dataset(df)
