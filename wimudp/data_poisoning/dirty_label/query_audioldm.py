import subprocess

import pandas as pd

from wimudp.data_poisoning.dirty_label.utils import CSV_CONCEPT_A_FILE, read_csv


def query_audioldm(df: pd.DataFrame):
    for _, row in df.iterrows():
        caption = row["caption"]
        subprocess.run(
            [
                "poetry",
                "run",
                "audioldm",
                "--model_name",
                "audioldm-s-full",
                "-t",
                f"'{caption}'",
            ]
        )


if __name__ == "__main__":
    df = read_csv(CSV_CONCEPT_A_FILE)
    query_audioldm(df)
