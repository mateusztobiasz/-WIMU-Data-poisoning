"""Module for creating wav audio files from librosa examples"""

import os

import librosa
import soundfile as sf


def create_wav(example_name: str, output_name: str) -> str:
    """Loading example from librosa in wav format"""

    try:
        audio_path = librosa.example(example_name)
    except librosa.util.exceptions.ParameterError:
        return ""

    y, sr = librosa.load(audio_path)
    output_path = (
        f"{os.getcwd()}/wimudp/watermarking/audio/examples/original/{output_name}.wav"
    )

    sf.write(output_path, data=y, samplerate=sr)
    return output_path
