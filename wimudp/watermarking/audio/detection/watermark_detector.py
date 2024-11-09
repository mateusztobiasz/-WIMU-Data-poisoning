from audioseal import AudioSeal
import torch
import torchaudio

def detect_watermark(audio_path, message_threshold=0.5):
    detector = AudioSeal.load_detector("audioseal_detector_16bits")
    audio, sample_rate = torchaudio.load(audio_path)
    audio = audio.unsqueeze(0)
    result, message = detector.detect_watermark(audio, sample_rate=sample_rate, message_threshold=message_threshold)
  
    print(f"Detection Result: {result} (probability of watermark)")
    print(f"Message: {message} (if present)")
    return result, message
