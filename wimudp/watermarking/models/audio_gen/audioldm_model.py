"""Module providing AudioLDM model"""

import subprocess

from models.audio_gen.base_model import BaseGenModel


class AudioLDMModel(BaseGenModel):
    """Class for AudioLDM model"""

    def generate_with_audio(self, audio_path: str) -> str:
        """Method for generating audio based on audio file using AudioLDM model"""

        subprocess.run(["audioldm", "-t", "dog barking loudly"], check=False)
        return ""

    def generate_with_text(self, text_prompt: str) -> str:
        return ""


cl = AudioLDMModel()
cl.generate_with_audio("dfsf")
