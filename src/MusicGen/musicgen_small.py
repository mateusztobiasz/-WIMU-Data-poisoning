import os

import soundfile as sf
import torch
from peft import PeftConfig, PeftModel
from transformers import (
    AutoModelForTextToWaveform,
    AutoProcessor,
    MusicgenForConditionalGeneration,
)


def generate():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained(
        "facebook/musicgen-small"
    ).to(device)

    inputs = processor(
        text=["80s punk and pop track with bassy drums and synth"],
        padding=True,
        return_tensors="pt",
    ).to(device)

    inputs = processor(
        text=["80s punk and pop track with bassy drums and synth"],
        padding=True,
        return_tensors="pt",
    ).to(device)

    audio_values = model.generate(**inputs, max_new_tokens=256)

    sampling_rate = model.config.audio_encoder.sampling_rate
    audio_values = audio_values.cpu().float().numpy()
    sf.write("punk_orig.wav", audio_values[0].T, sampling_rate)


def load():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    checkpoint_path = f"{os.getcwd()}/musicgen-dreamboothing/musicgen-small-lora-punk/"  # Replace with the actual path to your checkpoint directory

    config = PeftConfig.from_pretrained(checkpoint_path)
    base_model = AutoModelForTextToWaveform.from_pretrained(
        config.base_model_name_or_path, torch_dtype=torch.float16
    )

    model = PeftModel.from_pretrained(base_model, checkpoint_path).to(device)
    processor = AutoProcessor.from_pretrained(checkpoint_path)

    inputs = processor(
        text=["80s punk and pop track with bassy drums and synth"],
        padding=True,
        return_tensors="pt",
    ).to(device)

    audio_values = model.generate(**inputs, max_new_tokens=256)

    sampling_rate = model.config.audio_encoder.sampling_rate
    audio_values = audio_values.cpu().float().numpy()
    sf.write("punk_fined.wav", audio_values[0].T, sampling_rate)


if __name__ == "__main__":
    generate()
