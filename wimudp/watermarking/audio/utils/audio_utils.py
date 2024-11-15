"""Module defining AudioUtils class providing additional audio functions"""

import os

import librosa
import librosa.display as ld
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

EXAMPLES_PATH = f"{os.getcwd()}/wimudp/watermarking/audio/examples"


class AudioUtils:
    """Class for audio utils methods"""

    @staticmethod
    def create_wav(example_name: str) -> str:
        """Method for loading example from librosa in wav format"""

        try:
            audio_path = librosa.example(example_name)
        except librosa.util.exceptions.ParameterError:
            return ""

        y, sr = librosa.load(audio_path)
        output_path = f"{EXAMPLES_PATH}/original/{example_name}.wav"

        sf.write(output_path, data=y, samplerate=sr)
        return output_path

    @staticmethod
    def cut_wav(audio_path: str, seconds: int) -> str:
        """Method for cutting wav file to the desired number of seconds"""

        try:
            y, sr = librosa.load(audio_path, sr=None)
        except FileNotFoundError:
            return ""

        samples = int(seconds * sr)
        y_cut = y[:samples]

        audio_name = os.path.basename(audio_path)
        output_path = f"{EXAMPLES_PATH}/original/{seconds}_s_{audio_name}"

        sf.write(output_path, data=y_cut, samplerate=sr)
        return output_path

    @staticmethod
    def plot_wf_and_spec(audio_path: str) -> None:
        """Method for creating librosa waveform, fft and stft plots"""

        try:
            y, sr = librosa.load(audio_path, sr=None)
            filename = os.path.splitext(os.path.basename(audio_path))[0]
        except FileNotFoundError:
            return

        fft = np.fft.fft(y)
        fft = np.abs(fft)
        fft_freqs = np.fft.fftfreq(len(y), 1 / sr)

        stft = librosa.stft(y)
        stft = librosa.amplitude_to_db(np.abs(stft), ref=np.max)

        plt.figure(figsize=(20, 25))

        plt.subplot(3, 1, 1)
        ld.waveshow(y, sr=sr)
        plt.title("Waveform")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")

        plt.subplot(3, 1, 2)
        plt.plot(fft_freqs[: len(fft_freqs) // 2], fft[: len(fft) // 2])
        plt.title("FFT (Frequency Spectrum)")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")

        plt.subplot(3, 1, 3)
        ld.specshow(stft, sr=sr, x_axis="time", y_axis="hz", cmap="magma")
        plt.colorbar(format="%+2.0f dB")
        plt.title("Spectrogram (STFT)")
        plt.xlabel("Time (s)")
        plt.ylabel("Frequency (Hz)")

        plt.tight_layout()
        plt.savefig(f"{EXAMPLES_PATH}/plots/{filename}_fig.jpg")
