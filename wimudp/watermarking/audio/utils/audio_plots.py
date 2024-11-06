"""Module for plotting basic audio waveforms and spectograms"""

import os

import librosa
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")


def plot_wf_and_spec(audio_path: str) -> None:
    """Function for creating librosa plots once"""

    try:
        y, sr = librosa.load(audio_path, sr=None)
    except FileNotFoundError:
        return

    fft = np.fft.fft(y)
    fft = np.abs(fft)
    fft_freqs = np.fft.fftfreq(len(y), 1 / sr)

    stft = librosa.stft(y)
    stft = librosa.amplitude_to_db(np.abs(stft), ref=np.max)

    plt.figure(figsize=(20, 25))

    plt.subplot(3, 1, 1)
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 2)
    plt.plot(fft_freqs[: len(fft_freqs) // 2], fft[: len(fft) // 2])
    plt.title("FFT (Frequency Spectrum)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    plt.subplot(3, 1, 3)
    librosa.display.specshow(stft, sr=sr, x_axis="time", y_axis="hz", cmap="magma")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram (STFT)")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")

    plt.tight_layout()
    plt.savefig(f"{os.path.dirname(audio_path)}/{os.path.basename(audio_path)}_fig.jpg")
