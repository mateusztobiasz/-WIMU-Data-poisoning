import pandas as pd

AUDIOLDM_DATASET_DIR = "../finetuning/audioldm/data/dataset"
AUDIOS_DIR = f"{AUDIOLDM_DATASET_DIR}/audioset"
CONCEPT_A = "dog"
CONCEPT_C = "cat"
CONCEPT_A_ACTION = "bark"
CONCEPT_C_ACTION = "meow"
DATASET_DIR = "./data/datasets"
CSV_AUDIOCAPS_FILE = f"{DATASET_DIR}/audioset_train.csv"
CSV_CONCEPT_A_FILE = f"{DATASET_DIR}/audioset_{CONCEPT_A}.csv"
CSV_MISMATCHED_FILE = f"{AUDIOLDM_DATASET_DIR}/audioset_{CONCEPT_C}_{CONCEPT_A}.csv"
ROWS_NUMBER = 3000
THREADS_NUMBER = 20


def read_csv(csv_file: str) -> pd.DataFrame:
    df = pd.read_csv(csv_file, skipinitialspace=True)

    return df
