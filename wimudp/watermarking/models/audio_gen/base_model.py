"""Module implementing basic audio gen model interface"""

from abc import ABC, abstractmethod


class BaseGenModel(ABC):

    @abstractmethod
    def generate_audio(self, audio_path: str) -> str:
        """Abstract method for generating audio"""
        ...
