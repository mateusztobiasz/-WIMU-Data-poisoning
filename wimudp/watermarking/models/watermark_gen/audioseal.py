"""Module providing AudioSeal watermarking model"""

import os

import librosa
import soundfile as sf
import torch
from audio.utils.audio_utils import EXAMPLES_PATH
from audioseal import AudioSeal


def generate_watermark(audio_path: str) -> str:
    """Method for audio watermarking using AudioSeal generator"""

    y, sr = librosa.load(audio_path, sr=None)
    filename = os.path.splitext(os.path.basename(audio_path))[0]
    generator = AudioSeal.load_generator("audioseal_wm_16bits")

    y = torch.tensor(y)
    y = (y.unsqueeze(0)).unsqueeze(0)

    watermark = generator.get_watermark(y, sample_rate=sr)
    watermarked_y = y + watermark
    watermarked_y = watermarked_y.squeeze()

    output_path = f"{EXAMPLES_PATH}/watermarked/{filename}_wat.wav"
    sf.write(output_path, data=watermarked_y.detach().numpy(), samplerate=sr)

    return output_path


def detect_watermark(audio_path: str, message_threshold: float = 0.5) -> None:
    """Method for watermark detecting using AudioSeal detector"""

    y, sr = librosa.load(audio_path, sr=None)
    detector = AudioSeal.load_detector("audioseal_detector_16bits")

    y = torch.tensor(y)
    y = (y.unsqueeze(0)).unsqueeze(0)

    result, message = detector.detect_watermark(
        y, sample_rate=sr, message_threshold=message_threshold
    )

    print(f"Detection Result: {result} (probability of watermark)")
    print(f"Message: {message} (if present)")
