"""Module implementing basic audio gen model interface"""

from abc import ABC, abstractmethod


class BaseGenModel(ABC):
    """Class for base model"""

    @abstractmethod
    def generate_with_audio(self, audio_path: str) -> str:
        """Abstract method for generating audio based on audio file"""

    @abstractmethod
    def generate_with_text(self, text_prompt: str) -> str:
        """Abstract method for generating audio based on text prompt"""
