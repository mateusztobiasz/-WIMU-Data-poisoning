import pandas as pd

AUDIOLDM_DATASET_DIR = "../finetuning/audioldm/data/dataset"
AUDIOS_DIR = f"{AUDIOLDM_DATASET_DIR}/audioset"
CONCEPT_A = "dog"
CONCEPT_C = "cat"
CONCEPT_A_ACTION = "bark"
CONCEPT_C_ACTION = "meow"
DATA_DIR = "../data"
CSV_DATASET_FILE = f"{DATA_DIR}/audiocaps_train.csv"
AUDIOS_SAMPLES_DIR = f"{DATA_DIR}/audios"
CSV_CONCEPT_C_FILE = f"{DATA_DIR}/audiocaps_{CONCEPT_C}.csv"
CSV_NS_SAMPLES_FILE = f"{DATA_DIR}/{CONCEPT_C}_samples.csv"
CSV_MISMATCHED_FILE = f"{AUDIOLDM_DATASET_DIR}/audioset_{CONCEPT_C}_{CONCEPT_A}.csv"
ROWS_NUMBER = 3000
THREADS_NUMBER = 20
SAMPLES_NUMBER = 200


def read_csv(csv_file: str) -> pd.DataFrame:
    df = pd.read_csv(csv_file, skipinitialspace=True)

    return df
