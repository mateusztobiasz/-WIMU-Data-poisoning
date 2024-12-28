import pandas as pd
import torch
from torch.nn.functional import cosine_similarity

from wimudp.data_poisoning.nightshade.clap import CLAP
from wimudp.data_poisoning.utils import (
    CONCEPT_C,
    CONCEPT_C_ACTION,
    CSV_DATASET_FILE,
    CSV_NS_SAMPLES_FILE,
    SAMPLES_NUMBER,
    read_csv,
)


def get_samples() -> pd.DataFrame:
    df = read_csv(CSV_DATASET_FILE)
    similarities = calculate_similiarities(df)
    candidates = get_top_candidates(df, similarities)

    return candidates


def calculate_similiarities(df: pd.DataFrame) -> torch.Tensor:
    target_caption = [f"{CONCEPT_C} is {CONCEPT_C_ACTION}ing."]
    captions = df["caption"].to_list()
    clap = CLAP()

    target_caption_emb = clap.get_text_features(target_caption)
    captions_emb = clap.get_text_features(captions)

    return cosine_similarity(target_caption_emb, captions_emb)


def get_top_candidates(df: pd.DataFrame, similarities: torch.Tensor):
    candidates_indices = torch.argsort(similarities, descending=True)[:SAMPLES_NUMBER]
    candidates_df = pd.DataFrame(columns=["youtube_id", "caption"])

    for i in candidates_indices:
        index = i.item()
        candidates_df.loc[index] = [
            df.iloc[index]["youtube_id"],
            df.iloc[index]["caption"],
        ]

    return candidates_df


if __name__ == "__main__":
    samples = get_samples()

    samples.to_csv(CSV_NS_SAMPLES_FILE, index=False)
