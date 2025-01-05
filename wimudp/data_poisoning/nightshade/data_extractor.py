import os
import pandas as pd
import torch
from torch.nn.functional import cosine_similarity

from wimudp.data_poisoning.nightshade.clap import CLAP
from wimudp.data_poisoning.utils import (
    AUDIOS_SAMPLES_DIR,
    CONCEPT_C,
    CONCEPT_C_ACTION,
    CSV_CONCEPT_C_FILE,
    CSV_NS_SAMPLES_FILE,
    SAMPLES_NUMBER,
    read_csv,
)


def get_samples() -> pd.DataFrame:
    df = read_csv(CSV_CONCEPT_C_FILE)
    similarities = calculate_similiarities(df)
    candidates = get_top_candidates(df, similarities)

    return candidates


def calculate_similiarities(df: pd.DataFrame) -> torch.Tensor:
    target_caption = [f"{CONCEPT_C.capitalize()} is {CONCEPT_C_ACTION}ing"]
    captions = df["caption"].to_list()
    clap = CLAP()

    target_caption_emb = clap.get_text_features(target_caption)
    captions_emb = clap.get_text_features(captions)

    return cosine_similarity(target_caption_emb, captions_emb)


def get_top_candidates(df: pd.DataFrame, similarities: torch.Tensor):
    candidates_indices = torch.argsort(similarities, descending=True)[:SAMPLES_NUMBER]
    candidates_df = pd.DataFrame(columns=["audio", "caption"])

    for i in candidates_indices:
        index = i.item()
        if not check_audio_file(df.iloc[index]["youtube_id"]):
            continue

        candidates_df.loc[index] = [
            f"{df.iloc[index]['youtube_id']}.wav",
            df.iloc[index]["caption"],
        ]

    return candidates_df


def check_audio_file(youtube_id: str) -> bool:
    file_path = os.path.join(os.getcwd(), AUDIOS_SAMPLES_DIR, f"{youtube_id}.wav")

    return os.path.exists(file_path)


if __name__ == "__main__":
    samples = get_samples()

    samples.to_csv(CSV_NS_SAMPLES_FILE, index=False)
