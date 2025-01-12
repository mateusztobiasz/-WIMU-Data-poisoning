import argparse
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
    check_audio_file,
    read_csv,
)

def get_samples(concept_c: str, concept_c_action: str, samples_number: int) -> pd.DataFrame:
    df = read_csv(CSV_CONCEPT_C_FILE)
    similarities = calculate_similarities(df, concept_c, concept_c_action)
    candidates = get_top_candidates(df, similarities, samples_number)

    return candidates

def calculate_similarities(df: pd.DataFrame, concept_c: str, concept_c_action: str) -> torch.Tensor:
    target_caption = [f"{concept_c.capitalize()} is {concept_c_action}ing"]
    captions = df["caption"].to_list()
    clap = CLAP()

    target_caption_emb = clap.get_text_features(target_caption)
    captions_emb = clap.get_text_features(captions)

    return cosine_similarity(target_caption_emb, captions_emb)

def get_top_candidates(df: pd.DataFrame, similarities: torch.Tensor, samples_number: int):
    candidates_indices = torch.argsort(similarities, descending=True)[:samples_number]
    candidates_df = pd.DataFrame(columns=["audio", "caption"])

    for i in candidates_indices:
        index = i.item()
        if not check_audio_file(
            AUDIOS_SAMPLES_DIR, f"{df.iloc[index]['youtube_id']}.wav"
        ):
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
    parser = argparse.ArgumentParser(description="Generate samples with specified arguments.")
    parser.add_argument("--concept_c", type=str, default=CONCEPT_C, help="Value for CONCEPT_C (default: from utils)")
    parser.add_argument("--concept_c_action", type=str, default=CONCEPT_C_ACTION, help="Value for CONCEPT_C_ACTION (default: from utils)")
    parser.add_argument("--samples_number", type=int, default=SAMPLES_NUMBER, help="Value for SAMPLES_NUMBER (default: from utils)")

    args = parser.parse_args()

    samples = get_samples(args.concept_c, args.concept_c_action, args.samples_number)

    samples.to_csv(CSV_NS_SAMPLES_FILE, index=False)
