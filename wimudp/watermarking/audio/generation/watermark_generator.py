from audioseal import AudioSeal
import torch
import torchaudio

def generate_watermark(audio_path, alpha=1, output_path="watermarked_audio.wav"):
    model = AudioSeal.load_generator("audioseal_wm_16bits")
    audio, sample_rate = torchaudio.load(audio_path)
    watermarked_audio = model(audio.unsqueeze(0), sample_rate=sample_rate, alpha=alpha)
    torchaudio.save(output_path, watermarked_audio.detach().squeeze(0), sample_rate)
    return watermarked_audio
