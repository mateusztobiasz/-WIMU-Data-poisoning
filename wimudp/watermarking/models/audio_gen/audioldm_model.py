"""Module providing AudioLDM model"""

import os
import subprocess

from audio.utils.audio_utils import EXAMPLES_PATH
from models.audio_gen.base_model import BaseGenModel


class AudioLDMModel(BaseGenModel):
    """Class for AudioLDM model"""

    def generate_with_audio(self, audio_path: str) -> str:
        """Method for generating audio based on audio file using AudioLDM model"""

        subprocess.run(
            ["audioldm", "-f", f"{audio_path}", "-s", f"{EXAMPLES_PATH}/generated"],
            check=False,
        )

        filename = os.path.splitext(os.path.basename(audio_path))[0]
        base_path = f"{EXAMPLES_PATH}/generated/generation_audio_to_audio"
        gen_path = f"{base_path}/{filename}/{filename}.wav"
        output_path = f"{base_path}/{filename}/{filename}_gen.wav"

        os.rename(gen_path, output_path)
        return output_path

    def generate_with_text(self, text_prompt: str) -> str:
        return ""
