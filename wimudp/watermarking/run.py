"""Script for watermarking experiments"""

import os
from typing import Optional

from audio.utils.audio_utils import EXAMPLES_PATH, AudioUtils
from models.audio_gen.base_model import BaseGenModel
from models.audio_gen.musicgen_model import MusicGenModel
from models.watermark_gen.audioseal import detect_watermark, generate_watermark


class ExperimentRunner:

    def __init__(
        self,
        example_name: str,
        cut_seconds: int,
        gen_model: BaseGenModel,
        audio_path: Optional[str] = None,
    ) -> None:

        self.example_name = example_name
        self.cut_seconds = cut_seconds
        self.gen_model = gen_model
        self.audio_path = audio_path

    def __run_audio_utils_plot(self) -> None:
        """Private method for running audio utils in creating plots"""

        AudioUtils.plot_wf_and_spec(self.audio_path)

    def run_audio_utils_wav(self) -> None:
        """Method for running audio utils in creating wav files"""

        if self.audio_path is None:
            self.audio_path = AudioUtils.create_wav(self.example_name)

        self.audio_path = AudioUtils.cut_wav(self.audio_path, 30)
        self.original_path = self.audio_path

        self.__run_audio_utils_plot()

    def run_audio_generation(self) -> None:
        """Method for running audio generation"""

        self.audio_path = self.gen_model.generate_audio(self.audio_path)
        self.__run_audio_utils_plot()

    def run_watermark_generation(self) -> None:
        """Method for running watermark generation"""

        self.audio_path = generate_watermark(self.audio_path)
        self.watermarked_path = self.audio_path

        self.__run_audio_utils_plot()

    def run_watermark_detection(self) -> None:
        """Method for running watermark detection"""

        detect_watermark(self.original_path)
        detect_watermark(self.watermarked_path)
        detect_watermark(self.audio_path)

    def clean(self) -> None:
        """Method for cleaning generated files"""

        for root, _, files in os.walk(EXAMPLES_PATH):
            for file in files:
                os.remove(os.path.join(root, file))


if __name__ == "__main__":
    musicgen_model = MusicGenModel("small")
    experiment_runner = ExperimentRunner("trumpet", 30, musicgen_model)

    experiment_runner.clean()
    experiment_runner.run_audio_utils_wav()
    experiment_runner.run_watermark_generation()
    experiment_runner.run_audio_generation()
    experiment_runner.run_watermark_detection()
