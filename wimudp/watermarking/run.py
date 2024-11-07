"""Script for experimenting"""

from audio.generation import audio_generator
from audio.utils import audio_downloader, audio_plots
from models import musicgen


def run_experiment():
    """Function for running experiment"""

    audio_path = audio_downloader.create_wav("brahms", "brahms")
    audio_plots.plot_wf_and_spec(audio_path)

    model, processor = musicgen.get_model_and_processor("small")
    audio_gen_path = audio_generator.generate_audio(audio_path, model, processor)
    print(audio_gen_path)


if __name__ == "__main__":
    import os

    audio_plots.plot_wf_and_spec(
        os.getcwd() + "/wimudp/watermarking/audio/examples/generated/brahms_gen.wav"
    )
    # run_experiment()
