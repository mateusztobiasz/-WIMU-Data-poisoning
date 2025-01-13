import os

import pandas as pd

from wimudp.data_poisoning.utils import (
    AUDIOS_DIR,
    CONCEPT_A,
    CONCEPT_A_ACTION,
    CSV_CONCEPT_C_FILE,
    CSV_MISMATCHED_FILE,
    check_audio_file,
    read_csv,
)


def mismatch_caption(row: pd.Series) -> str:
    row["caption"] = f"{CONCEPT_A.capitalize()} is {CONCEPT_A_ACTION}ing."

    return row["caption"]


def create_dirty_label_dataset(df: pd.DataFrame):
    dirty_label_df = pd.DataFrame(columns=["audio", "caption"])

    for id, row in df.iterrows():
        file_exists = check_audio_file(AUDIOS_DIR, f"{row['youtube_id']}.wav")

        if file_exists:
            mismatched_caption = mismatch_caption(row)
            dirty_label_df.loc[id] = [f"{row['youtube_id']}.wav", mismatched_caption]

    dirty_label_df.to_csv(
        CSV_MISMATCHED_FILE,
        index=False,
    )


if __name__ == "__main__":
    df = read_csv(CSV_CONCEPT_C_FILE)
    create_dirty_label_dataset(df)
