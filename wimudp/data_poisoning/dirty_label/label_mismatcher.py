import os
import re

import pandas as pd

from wimudp.data_poisoning.dirty_label.utils import (
    AUDIOS_DIR,
    CONCEPT_A,
    CONCEPT_C,
    CONCEPT_A_ACTION,
    CONCEPT_C_ACTION,
    CSV_CONCEPT_A_FILE,
    CSV_MISMATCHED_FILE,
    read_csv,
)

LABELS_MAPPING = {
    CONCEPT_A: CONCEPT_C,
    CONCEPT_A.capitalize(): CONCEPT_C.capitalize(),
    CONCEPT_A_ACTION: CONCEPT_C_ACTION,
    CONCEPT_A_ACTION.capitalize(): CONCEPT_C_ACTION.capitalize(),
}


def check_audio_file(row: pd.Series) -> bool:
    file_path = os.path.join(os.getcwd(), AUDIOS_DIR, f"{row['youtube_id']}.wav")

    return os.path.exists(file_path)


def mismatch_caption(row: pd.Series) -> str:
    for old, new in LABELS_MAPPING.items():
        row["caption"] = row["caption"].replace(old, new)
    
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
