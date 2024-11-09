from audioseal import AudioSeal
import torch
import torchaudio

def generate_watermark(audio_path, alpha=1, output_path="watermarked_audio.wav"):
    model = AudioSeal.load_generator("audioseal_wm_16bits")
    audio, sample_rate = torchaudio.load(audio_path)
    audio = audio.unsqueeze(0) 
    watermark = model.get_watermark(audio, sample_rate=sample_rate)
    watermarked_audio = audio + watermark * alpha
    watermarked_audio = watermarked_audio.squeeze(0)
    torchaudio.save(output_path, watermarked_audio.detach(), sample_rate)
    
    return watermarked_audio
