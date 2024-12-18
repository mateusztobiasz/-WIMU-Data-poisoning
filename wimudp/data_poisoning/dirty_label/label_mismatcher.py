import os
import re

import pandas as pd

from wimudp.data_poisoning.dirty_label.utils import (
    AUDIOLDM_DATASET_DIR,
    AUDIOS_DIR,
    CONCEPT_A,
    CONCEPT_C,
    CSV_CONCEPT_C_FILE,
    CSV_MISMATCHED_FILE,
    read_csv,
)

LABELS_MAPPING = {
    CONCEPT_C: CONCEPT_A,
    "barks": "meows",
    "barking": "meowing",
    "whimpers": "yowls",
    "whimpering": "yowling softly",
    "growls": "hisses",
    "growling": "hissing aggressively",
    "pants": "purrs",
    "panting": "purring",
    "howls": "yowls",
    "howling": "yowling",
    "whines": "meows plaintively",
    "whining": "meowing sadly",
    "yips": "chirps",
    "yipping": "chirping",
    "grunts": "purring softly",
    "yelping": "yowling loudly",
    "yelps": "yowls",
    "crying": "crying softly",
    "cries": "meows in distress",
    "woofs": "meows loudly",
    "trots": "scurries gracefully",
    "steps": "pads softly",
    "walks": "pads gently",
    "rubs": "rubs against",
    "scratches": "scratches softly",
}


def check_audio_file(row: pd.Series) -> bool:
    file_path = os.path.join(os.getcwd(), AUDIOS_DIR, f"{row['youtube_id']}.wav")

    return os.path.exists(file_path)


def mismatch_caption(row: pd.Series) -> str:
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(key) for key in LABELS_MAPPING.keys()) + r")\b"
    )

    return pattern.sub(lambda match: LABELS_MAPPING[match.group(0)], row["caption"])


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
    df = read_csv(CSV_CONCEPT_C_FILE)
    create_dirty_label_dataset(df)
