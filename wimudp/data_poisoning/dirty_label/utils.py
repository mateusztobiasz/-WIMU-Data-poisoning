import pandas as pd

AUDIOLDM_DATASET_DIR = "../finetuning/audioldm/data/dataset"
AUDIOS_DIR = f"{AUDIOLDM_DATASET_DIR}/audioset"
CONCEPT_A = "cat"
CONCEPT_C = "dog"
DATASET_DIR = "./data/datasets"
CSV_AUDIOCAPS_FILE = f"{DATASET_DIR}/audiocaps_train.csv"
CSV_CONCEPT_C_FILE = f"{DATASET_DIR}/audiocaps_{CONCEPT_C}.csv"
CSV_MISMATCHED_FILE = f"{AUDIOLDM_DATASET_DIR}/audiocaps_{CONCEPT_C}_{CONCEPT_A}.csv"
ROWS_NUMBER = 330
THREADS_NUMBER = 10


def read_csv(csv_file: str) -> pd.DataFrame:
    df = pd.read_csv(csv_file)

    return df
