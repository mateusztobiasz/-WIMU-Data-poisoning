"""Module providing MusicGen model and its processor"""

from typing import Tuple

import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
musicgen_types = {
    "small": "facebook/musicgen-small",
    "melody": "facebook/musicgen-melody",
    "large": "facebook/musicgen-large",
}


def get_model_and_processor(
    musicgen_type: str,
) -> Tuple[MusicgenForConditionalGeneration, AutoProcessor]:
    """Return specified MusicGen model and its processor"""

    try:
        musicgen_type = musicgen_types[musicgen_type]
    except KeyError:
        return None, None

    model = MusicgenForConditionalGeneration.from_pretrained(musicgen_type).to(device)
    processor = AutoProcessor.from_pretrained(musicgen_type)

    return model, processor
