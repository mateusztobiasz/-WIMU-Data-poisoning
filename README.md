# WIMU-Data-poisoning
Project developed as an approach to data poisoning for music generative models using musically-aware adversarial attacks.
## Design proposal
### Schedule
- Week 1 (02.10 - 08.10): - 
- **Week 2 (09.10 - 15.10):** Nighshade/Glaze research
- **Week 3 (16.10 - 22.10):** Watermarking research/design proposal submission
- **Week 4 (23.10 - 29.10):** Preparing environment
- **Week 5 (30.10 - 05.11):** Generating and detecting watermarking in music generative models (*)
- **Week 6 (06.11 - 12.11):** Preparing dataset for simple "dirty-label" attack and analyzing results
- **Week 7 (13.11 - 19.11):** Preparing detailed attack design 
- **Week 8 (20.11 - 26.11):** Selecting poison text prompts (pt. I)
- **Week 9 (27.11 - 03.12):** Selecting poison text prompts (pt. II)
- **Week 10 (04.12 - 10.12):** Generating audio files based on selected text prompts
- **Week 11 (11.12 - 17.12):** Constructing poison audio files (pt. I)
- **Week 12 (18.12 - 24.12):** Constructing poison audio files (pt. II)
- **Week 13 (25.12 - 31.12):** Constructing poison audio files (pt. III)
- **Week 14 (01.01 - 07.01):** Fine-tuning models on prepared poison dataset
- **Week 15 (08.01 - 14.01):** Testing and evaluation 
- **Week 16 (15.01 - 21.01):** Project submission
- Week 17 (22.01 - 28.01): -

(*) It means, If watermarking the data and verifying whether generative models like VampNet, MusicGen, or SampleRNN reproduce the watermark proves to be straightforward, we will proceed with implementing Nightshade for audio. However, if watermarking turns out to be more complex, we will change our schedule to solve the watermarking issue.
### Models
| **Model** | **Author** | **Module**  | **Type**  | **Fine-tuning**  |
|:-:|:-:|:-:|:-:|:-:|
| MusicGen Small | Facebook  | transformers  | TTA  | Yes, via: [MusicGen dreamboothing](https://github.com/ylacombe/musicgen-dreamboothing)|
|  AudioSeal | Meta   | ResNet + LSTM  |  Watermarking Model | Yes, via: [AudioSeal](https://github.com/facebookresearch/audioseal/blob/main/docs/TRAINING.md)   | 
|  VampNet | Hugo Flores García and Prem Seetharaman  | LSTM + Transformer   | Generative Model  | Yes, via: [VampNet](https://github.com/hugofloresgarcia/vampnet)     |
|  MusicGen | Facebook | Transformer   | Generative Model  | Yes, via: [MusicGen](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)       | 
|  SampleRNN | Soroush Mehri  | RNN  | Generative Model  | Yes, via: [SampleRNN](https://github.com/facebookresearch/audiocraft/tree/main)   | 
### Approach
Based on our research, we tend to focus on fine-tuning pre-trained text-to-audio (we also consider text-to-speech) models rather than training a clear model on huge datasets. The main factor is long time required to achieve so and need to use sophisticated graphic cards. Based on paper describing Nightshade we think that our approach is reasonable and even closer to real conditions.

### Bibliography
- AudioSeal: https://arxiv.org/abs/2401.17264v2 / https://github.com/facebookresearch/audioseal/tree/main
- VampNet: https://arxiv.org/abs/2307.04686 / https://github.com/hugofloresgarcia/vampnet
- MusicGen: https://arxiv.org/abs/2306.05284 / https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md
- SampleRNN: https://arxiv.org/abs/1612.07837 / https://github.com/soroushmehr/sampleRNN_ICLR2017/tree/master
