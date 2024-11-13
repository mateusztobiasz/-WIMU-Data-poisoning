"""Module providing MusicGen model and its processor"""

import os

import librosa
import soundfile as sf
import torch
from audio.utils.audio_utils import EXAMPLES_PATH
from models.audio_gen.base_model import BaseGenModel
from transformers import AutoProcessor, MusicgenForConditionalGeneration

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
musicgen_types = {
    "small": "facebook/musicgen-small",
    "melody": "facebook/musicgen-melody",
    "large": "facebook/musicgen-large",
}


class MusicGenModel(BaseGenModel):
    def __init__(self, musicgen_type: str) -> None:
        try:
            musicgen_type = musicgen_types[musicgen_type]
        except KeyError:
            musicgen_type = musicgen_type[0]

        self.model = MusicgenForConditionalGeneration.from_pretrained(musicgen_type).to(
            device
        )
        self.processor = AutoProcessor.from_pretrained(musicgen_type)

    def generate_audio(self, audio_path: str) -> str:
        """Method for generating audio using MusicGen model"""

        y, sr = librosa.load(audio_path, sr=32000)
        filename = os.path.splitext(os.path.basename(audio_path))[0]
        y_ten = torch.tensor(y).to(device)

        inputs = self.processor(
            audio=y_ten,
            sampling_rate=sr,
            padding=True,
            return_tensors="pt",
        ).to(device)

        audio_values = self.model.generate(**inputs, max_new_tokens=128)
        audio_values = audio_values.cpu().float().numpy()

        output_path = f"{EXAMPLES_PATH}/generated/{filename}_gen.wav"
        sf.write(output_path, audio_values[0].T, sr)

        return output_path
