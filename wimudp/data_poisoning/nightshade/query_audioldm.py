import subprocess

import pandas as pd

from wimudp.data_poisoning.utils import (
    AUDIOS_SAMPLES_DIR,
    CONCEPT_A,
    CONCEPT_A_ACTION,
    CSV_NS_SAMPLES_FILE,
    read_csv,
)


def query_audioldm(df: pd.DataFrame):
    caption = f"{CONCEPT_A.capitalize()} is {CONCEPT_A_ACTION}ing"
    subprocess.run(
        [
            "poetry",
            "run",
            "audioldm",
            "--model_name",
            "audioldm-s-full",
            "-t",
            f"'{caption}'",
            "-s",
            AUDIOS_SAMPLES_DIR,
        ]
    )


if __name__ == "__main__":
    df = read_csv(CSV_NS_SAMPLES_FILE)
    query_audioldm(df)
