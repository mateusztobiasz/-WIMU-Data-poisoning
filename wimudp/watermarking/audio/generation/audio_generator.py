"""Module for generating audio based on audio prompt"""

import os

import librosa
import soundfile as sf
import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def generate_audio(
    audio_path: str, model: MusicgenForConditionalGeneration, processor: AutoProcessor
) -> str:
    """Function for generating audio using MusicGen models"""

    y, sr = librosa.load(audio_path, sr=32000)
    y_ten = torch.tensor(y).to(device)
    y_ten = y_ten[: len(y) // 2]

    inputs = processor(
        audio=y_ten,
        sampling_rate=sr,
        padding=True,
        return_tensors="pt",
    ).to(device)

    audio_values = model.generate(**inputs, max_new_tokens=512)
    audio_values = audio_values.cpu().float().numpy()

    output_path = f"""{os.path.dirname(os.path.dirname(audio_path))}/generated/,
    {os.path.splitext(os.path.basename(audio_path))[0]}_gen.wav"""
    sf.write(output_path, audio_values[0].T, sr)

    return output_path
