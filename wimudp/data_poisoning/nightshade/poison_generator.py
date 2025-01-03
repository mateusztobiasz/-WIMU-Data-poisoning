import pandas as pd
import torch
import threading

from wimudp.data_poisoning.nightshade.pipeline import Pipeline
from wimudp.data_poisoning.nightshade.vocoder import Vocoder
from wimudp.data_poisoning.utils import CSV_NS_SAMPLES_FILE, AUDIOS_SAMPLES_DIR, AUDIOS_GEN_DIR, read_csv, pad_waveforms, normalize_tensor

MAX_EPOCHS = 300
EPS = 0.05


def generate_poison(row: pd.Series, vocoder: Vocoder, pipeline: Pipeline) -> torch.Tensor:
    w_1 = vocoder.load_audio(f"{AUDIOS_SAMPLES_DIR}/{row['youtube_id']}.wav")
    w_2 = vocoder.load_audio(f"{AUDIOS_SAMPLES_DIR}/big.wav")

    w_1, w_2 = pad_waveforms(w_1, w_2)
    w_1_mel = vocoder.gen_mel(w_1)
    w_2_mel = vocoder.gen_mel(w_2)
    w_1_mel_norm = normalize_tensor(w_1_mel)
    w_2_mel_norm = normalize_tensor(w_2_mel)

    target_latent = pipeline.get_latent(w_2_mel_norm)
    target_latent = target_latent.detach()

    delta = torch.clone(w_1_mel_norm) * 0.0
    max_change = EPS * 2
    step_size = max_change

    for i in range(MAX_EPOCHS):
        actual_step_size = step_size - (step_size - step_size / 100) / MAX_EPOCHS * i
        delta.requires_grad_()

        pert_mel = torch.clamp(delta + w_1_mel_norm, -1, 1)
        per_latent = pipeline.get_latent(pert_mel)
        diff_latent = per_latent - target_latent

        loss = diff_latent.norm()
        grad = torch.autograd.grad(loss, delta)[0]

        delta = delta - torch.sign(grad) * actual_step_size
        delta = torch.clamp(delta, -max_change, max_change)
        delta = delta.detach()

        if i % 20 == 0:
            print(f"Loss: {loss}")

    final_mel_norm = torch.clamp(delta + w_1_mel_norm, -1, 1)
    return normalize_tensor(final_mel_norm, True, w_1_mel.max(), w_1_mel.min())
    

def generate_all(df: pd.DataFrame):
    vocoder = Vocoder()
    pipeline = Pipeline()

    for _, row in df.iterrows():
        final_mel = generate_poison(row, vocoder, pipeline)
        final_wav = vocoder.gen_wav(final_mel)
        vocoder.save_audio(final_wav, f"{AUDIOS_GEN_DIR}/{row['youtube_id']}.wav")


if __name__ == "__main__":
    df = read_csv(CSV_NS_SAMPLES_FILE)
    generate_all(df)