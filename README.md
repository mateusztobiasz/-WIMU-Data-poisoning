# WIMU-Data-poisoning
## Description
Project developed as an approach to data poisoning for music generative models using musically-aware adversarial attacks.
## Setup
### Prerequisites
- You need *Python 3.11.0* or higher to work with the project 
- Make sure you have *poetry* installed as we use this tool to build the project and manage its dependencies
### Cloning
The first thing you want to do is to clone our repository using:
```bash
foo@bar:~$: git clone https://github.com/WIMU-BKT/WIMU-Data-poisoning.git
```
And then:
```bash
foo@bar:~$ cd WIMU-Data-poisoning/
```
### Environment and dependencies
To create a virtual environment use (*python* is a name of at least Python 3.12.0 executable):
```bash
foo@bar:~/WIMU-Data-poisoning$ poetry env use python
```
To make sure it is set up properly, run (an expected output is shown below):
```bash
foo@bar:~/WIMU-Data-poisoning$ poetry env list
.venv (Activated)
```
To install the project and its dependencies run:
```bash
foo@bar:~/WIMU-Data-poisoning$ poetry install
```
However, there is a shorter way to set thing up. You can create an environment and install required packages by simply running:
```bash
foo@bar:~ export PYTHON_EXEC=<name_of_python_executable>
foo@bar:~ make venv
```
### Packages
We use *poetry* to manage our dependencies. Therefore if your changes require adding new packages run:
```bash
foo@bar:~/WIMU-Data-poisoning$ poetry add <package_name>
```
This command adds a new package to *pyproject.toml* and *poetry.lock* files. Poetry manages them by itself so **DO NOT CHANGE** these files manually because it may cause problems with synchronization.
### Linters
If you want to contribute to our project, your pull request must pass our linter pipeline. In order to check your source code run:
```bash
foo@bar:~ make <black|sort|mypy|flake|pylint>
``` 
## Project structure
### Root dir
In the root dir there are basically common files for python projects such as pyproject.toml and poetry.lock for dependencies management or Makefile to run linters easier.
### Watermarking
In `wimudp/watermarking` there are files responsible for watermarking experiments. In the main dir you can find 2 files:
- `run.py` - command-line tool responsible for running other scripts
- `watermark_notebook.ipynb` - Jupyter notebook created in order to run watermarking experiments on Google Colab
  
In `wimudp/watermarking/audio` directory there are:
- `utils` - containing script responsible for performing audio specific actions such as: waveform or spectrograms generation
- `examples` - basically a place for storing generated and watermarked .wav files

On the other hand, in `wimudp/watermarking/models` there are:
- `audio_gen` - dir containing files defining audio generative models - AudioLDM and MusicGen
- `watermark_gen` - dir containing file defining AudioSeal model
### Data poisoning
In `wimudp/data_poisoning` there are three files:
- `generate_dirty_label.py` - command line tool used for running 3 steps to generate dirty label samples
- `generate_nightshade.py` - command line tool used for running 3 stepes to generate Nightshade samples
- `utils.py` - defining constant values and common methods

In `wimudp/data_poisoning/data` there are dataset files where samples are chosen from.

In `wimudp/data_poisoning/dirty_label` there are three files which are used to prepare dirty label attack:
- `dataset_filter.py` - responsible for dataset filtering
- `audio_loader.py` - responsible for downloading audio files based on youtube_id
- `label_mismatcher.py` - responsible for captions mismacthing
- `dirtylabel_notebook.ipynb` - notebook created to perform dirty label attack on Google Colab

In `wimudp/data_poisoning/nightshade` there are three files which are used to prepare Nightshade attack:
- `data_extractor.py` - responsible for prompts extraction (according to Step 1 from Nightshade paper)
- `audioldm_prompter.py` - responsbile for querying AudioLDM model (according to Step 2 from Nightshade paper)
- `poison_generator.py` - responsbile for poison samples generation (according to Step 3 from Nightshade paper)
- `nightshade_notebook.ipynb` - notebook created to perform Nightshade attack on Google Colab
- `pipeline.py` - defining AudioLDM pipeline, used for VAE embeddings
- `clap.py` - defining CLAP model
- `vocoder.py` - defining WaveGlowVocoder model

In `wimudp/data_poisoning/finetuning` there is a git submodule which is basically a fork of AudioLDM finetuning script. It is used for pretrained AudioLDM finetuning with poison samples.

## Design proposal
### Schedule
| **Week** | **TO-DO** |
|:-:|:-:|
|Week 1 (02.10 - 08.10)|  - |
|Week 2 (09.10 - 15.10)|  Nighshade/Glaze research|
|Week 3 (16.10 - 22.10)|  Watermarking research/design |proposal submission |
|Week 4 (23.10 - 29.10)| Preparing environment |
|Week 5 (30.10 - 05.11)| Generating and detecting watermarking in music generative models **(*)** |
|Week 6 (06.11 - 12.11)| Preparing dataset for simple "dirty-label" attack and analyzing results |
|Week 7 (13.11 - 19.11)| Preparing detailed attack design |
|Week 8 (20.11 - 26.11)| Selecting poison text prompts (pt. I) |
|Week 9 (27.11 - 03.12)| Selecting poison text prompts (pt. II) |
|Week 10 (04.12 - 10.12)| Generating audio files based on selected text prompts |
|Week 11 (11.12 - 17.12) |Constructing poison audio files (pt. I) |
|Week 12 (18.12 - 24.12) |Constructing poison audio files (pt. II) |
|Week 13 (25.12 - 31.12) |Constructing poison audio files (pt. III) |
|Week 14 (01.01 - 07.01) |Fine-tuning models on prepared poison dataset |
|Week 15 (08.01 - 14.01) |Testing and evaluation |
|Week 16 (15.01 - 21.01) |Project submission |
|Week 17 (22.01 - 28.01) |- |

**(*)** It means, If watermarking the data and verifying whether generative models like VampNet, MusicGen, or SampleRNN reproduce the watermark proves to be straightforward, we will proceed with implementing Nightshade for audio. However, if watermarking turns out to be more complex, we will decide whether to proceed with Nightshade for audio or focus on resolving the watermarking issue.
### Approach and planned experiments for Nightshade
Based on our research, we plan to focus on fine-tuning pre-trained text-to-audio models (we are also considering text-to-speech models) rather than training a model from scratch on large datasets. The main reason for this is the extended time required for training from scratch, along with the need for sophisticated graphics cards. We believe our approach is reasonable, and closer to real-world conditions, as suggested in the Nightshade paper.

If we proceed with reproducing Nightshade for audio, Our first step will be to empirically validate the effectiveness of a "dirty-label" poisoning attack on music generative models that we have identified. To measure the success of the attack, we will use two metrics: a CLAP-based similarity score and human inspection.

Following this, we will attempt to reproduce the Nightshade attack, adapting the three steps presented in the original paper by replacing image-specific elements with their audio equivalents. As with the "dirty-label" attack, we will validate our results using the two metrics mentioned above.

Once we have the outcomes for both attacks, we plan to compare their effectiveness, as well as the number of poisoned samples required for each.

### Functionality for Nightshade
Our main goal is to reproduce a similar attack to Nightshade, but for music generative models. We aim to test the effectiveness of this approach, which theoretically should outperform the simpler "dirty-label" attack. Additionally, we plan to develop a specific CLI tool to automate the process of generating poisoned samples for selected music genres and fine-tuning the target model.
### **(*)** Approach and planned experiments for Watermarking
We will use the AudioSeal model to generate a permanent watermark for audio files. The experimental steps are as follows:

Adding a permanent watermark to audio data:
We will generate a permanent watermark using the AudioSeal model, which will be embedded in the original audio files. The watermark will be designed to be resistant to fading and present in all processed forms of the sound.

Verification of the watermark in audio generated by generative models:
The next step will be to check whether the watermark remains detectable in audio generated by various generative models. The goal of this stage will be to assess how effectively the watermark is transferred to the generated audio.

Evaluation of the watermark:
We will evaluate the watermark using two key metrics: True Positive Rate (TPR) and False Positive Rate (FPR). TPR will indicate how effectively the watermark is detected in cases where it should be present, while FPR will help assess the number of false detections, or instances where the watermark was detected in audio where it should not be.

Watermark removal attempts:
The final stage of the experiments will involve simulating attacks aimed at removing the watermark from processed audio (known as "Watermark-removal attacks"). Evaluating these attempts will help determine the resistance of our watermark to various removal techniques.
### **(*)** Functionality for Watermarking
The main function of our program will be to generate a watermark for audio that is resistant to fading. This means that the watermark added to the audio data will also be present in audio generated by generative models such as VampNet, MusicGen, SampleRNN, or other models, allowing for the protection of copyright for the creators of musical works.
### Models
| **Model** | **Author** | **Module**  | **Type**  | **Fine-tuning**  |
|:-:|:-:|:-:|:-:|:-:|
| MusicGen  | Facebook  | transformers  | TTA  | Yes, via: [MusicGen dreamboothing](https://github.com/ylacombe/musicgen-dreamboothing)|
|  AudioSeal | Meta   | audioseal   | ATA | Yes, via: [AudioSeal](https://github.com/facebookresearch/audioseal/blob/main/docs/TRAINING.md)   | 
|  VampNet | Hugo Flores García and Prem Seetharaman  | Directly from: [VampNet](https://github.com/hugofloresgarcia/vampnet)   | ATA   | Yes, via: [VampNet](https://github.com/hugofloresgarcia/vampnet)     |
|  SampleRNN | Soroush Mehri  | Directly from: [SampleRNN](https://github.com/soroushmehr/sampleRNN_ICLR2017/tree/master)  | ATA | Yes, via: [SampleRNN](https://github.com/soroushmehr/sampleRNN_ICLR2017/tree/master)   |
|  CLAP | LAION-AI  | transformers  | multimodal  | Yes, via: [CLAP](https://github.com/LAION-AI/CLAP)   | 

### Technology stack
1. Python
   - transformers
   - torch
   - torchaudio
   - torchvision
   - soundfile
2. Git
3. GitHub
4. Huggingface
5. Poetry
6. Google Colab
7. Jupyter notebook
## Watermarking Experiment 
AudioSeal ia  a cutting-edge solution that leverages localized watermarking to detect AI-generated speech with precision. Instead of relying on passive detection, AudioSeal proactively embeds a watermark into the speech signal, which can be later detected to verify the authenticity of the content. The particularity of AudioSeal is that the watermark detection is localized. The detector directly predicts for each time step (1/16k of a second) if the watermark is present or not, which makes it ultra fast and suitable for real-time applications.

AudioSeal is primarily designed for embedding watermarks in speech signals, however, in the following sections, we will explore how it performs in embedding watermarks into audio files and detecting them in generative model-produced audio.

### How does it work?
![image](https://github.com/user-attachments/assets/2a8dd339-7fad-42f1-b58b-b0423bed3bf9)
AudioSeal consists of two main components:
- A generator, which generate an additive watermark waveform based on the input audio,
- A detector, which predicts the presence of the watermark at each time step.

The generator is trained to produce a watermark that is imperceptible to the human ear, and robust to common audio processing operations such as compression, re-encoding, and noise addition. The detector is trained to predict the presence of the watermark at each time step, and is designed to be fast and suitable for real-life applications where watermarked audio is embedded in a stream of (often non-watermarked) audio.

### Model architectures
![image](https://github.com/user-attachments/assets/181e4218-a830-482b-9c8f-eff7b2d971d6)
The architecture of the generator and detector models is based on the EnCodec design. The generator consists of an encoder and a decoder, both incorporating elements from EnCodec. The encoder applies a 1D convolution followed by four convolutional blocks, each including a residual unit and down-sampling layer. The decoder mirrors the encoder structure but uses transposed convolutions instead.

The detector comprises an encoder, a transposed convolution, and a linear layer. The encoder shares the generator’s architecture but with different weights. The transposed convolution upsamples the activation map to the original audio resolution, and the linear layer reduces the dimensions to two, followed by a softmax function that gives sample-wise probability scores.

### Detection, Localization, Attribution
The detector is designed to predict the presence of the watermark and optional bits at each time step.
This allows for:

- Detection: we use a threshold on the average detector’s output to decide if the watermark is present or not.  (default: 0.5) 
- Localization: we use a threshold on the detector’s output to decide if the watermark is present at each time step.  (default: 0.5)
- Attribution: we use the optional bits to attribute the audio to a specific model or version.  (default: 0.5)
### Generative Models
In our watermarked experiment, we use the MusicGen model and the AudioLDM model
#### MusicGen Model
MusicGen, introduced by Meta AI, is a controllable music generation model that combines a single-stage autoregressive transformer with compressed discrete music tokenization. Unlike traditional multi-stage methods, MusicGen provides high-quality music outputs conditioned on text or melody, achieving efficient and precise control over various musical attributes like harmony, genre, and instruments. It supports stereo and monophonic generation, making it versatile for diverse musical applications​
#### AudioLDM Model
AudioLDM is a diffusion model that focuses on generating high-fidelity audio by translating textual prompts into a "language of audio" (LOA). The framework uses self-supervised learning to extract semantic and acoustic representations via an AudioMAE model and combines them with GPT-2 for conditional generation. AudioLDM supports various audio generation tasks, including text-to-audio, text-to-music, and text-to-speech, achieving state-of-the-art results in producing realistic and intelligible audio. Its flexibility and generality enable application across different audio domains​
### Main results
The STFT, FFT, and waveform are generated in the wimudp/watermarking/audio/examples directory
#### MusicGen

| Audio Name                  | Detection Result     | Probability of Watermark |
|-----------------------------|----------------------|--------------------------|
| 30_s_trumpet.wav            | 0.0 | Very Low                      |
| 30_s_trumpet_wat.wav        | 1.0 | High                     |
| 30_s_trumpet_wat_gen.wav    | 0.0011080994736403227 | Very Low                 |

You have to run experiment locally using our scripts on repo
#### AudioLdm

| Audio Name                  | Detection Result     | Probability of Watermark |
|-----------------------------|----------------------|--------------------------|
| 30_s_trumpet.wav            | 0.07275416702032089 | Low                      |
| 30_s_trumpet_wat.wav        | 0.999527096748352   | High                     |
| 30_s_trumpet_wat_gen.wav    | 0.01933826319873333 | Very Low                 |

[Notebook with tests](https://github.com/WIMU-BKT/WIMU-Data-poisoning/blob/audioldm-finetuning/wimudp/watermarking/watermark_notebook.ipynb)
### Conclusions
The experiments related to watermark detection in generated audio have revealed several key findings:

**Undetectability of the watermark in certain cases:**
Results show that the watermark, although embedded in the original audio, often becomes nearly undetectable in audio generated by generative models such as MusicGen and AudioLDM. For instance, in the audio generated by MusicGen, the probability of detecting the watermark was very low (0.001).

**Impact of model architecture:**
The detectability of the watermark depends on the architecture of the generative model and how these models process the input data. Models like AudioLDM and MusicGen modify the audio signal to varying degrees, which affects the transfer and detectability of the watermark.

**Watermark resilience:**
Although the watermark is designed to resist compression, re-encoding, and noise addition, its effectiveness in generative audio decreases significantly. Notably, results for directly watermarked audio files (e.g., 30_s_trumpet_wat.wav) show high watermark detectability (close to 1.0), confirming its presence in the original file.

**Future challenges:**
To improve watermark effectiveness, it may be necessary to adapt watermarking methods to the specific characteristics of generative models. This could involve designing more advanced watermarking techniques that are more resilient to the modifications introduced by generative audio models.

In summary, while the watermark performs effectively in original audio files, its detectability in audio processed by generative models remains limited. Further research should focus on developing methods to enhance the resilience of the watermark against changes introduced by different model architectures.
## Data poisoning experiments
### Description
After watermarking experiment results, we decided to focus on data poisoning experiments. In order to acquire the necessary knowledge, we've read two papers - [Glaze](https://www.usenix.org/system/files/usenixsecurity23-shan.pdf) and [Nightshade](https://arxiv.org/pdf/2310.13828). Our main goal was to recreate data poisoning attack in audio generative models so we had to choose one paper which we were going to follow. After lively discussion we decided to focus on Nightshade. In order to recreate the similiar attack, we decided to follow each section from the Nightshade paper and adjust them to audio generation approach.
### Approach
In introduction authors introduced two scenarios: training a model from the scratch and continuously training a pre-trained model. The first approach can be really expensive (authors gave example of 150K GPU hours). Therefore, we chose the second option. In the next sections we learnt that Nightshade attack aims diffusion models. Thats's the reason why we decided to concentrate only on one audio diffusion model - [AudioLDM](https://github.com/haoheliu/AudioLDM]).
### Dataset
Nightshade's authors examined LAION-Aesthetic which is one of the most popular open-source dataset for training text-to-image models. We also chose one dataset for our purposes - AudioCaps (in the future we might also add MusicCaps which is quite similar to AudioCaps but focuses more on music files). It is one of the most famous datasets for training text-to-audio models and according to [AudioLDM paper](https://arxiv.org/pdf/2301.12503) it was used to train this model.
### Concept sparsity
In Nightshade's paper authors examined LAION-Aesthetic dataset to show the concept sparsity - property of a dataset where a given concept is only relevant or present in a small subset of the data samples. We decided to do the same thing and use two metrics - word frequency and semantic frequency. Our progress in this field can be seen in this [notebook](https://github.com/WIMU-BKT/WIMU-Data-poisoning/blob/dirty-label-attack-analysis/wimudp/data-poisoning/dirty-label-attack/dirty-label-analysis.ipynb).
### Dirty-label attack
Following what Nightshade's authors did first, we want to conduct the dirty label attack. In order to achieve this we want to create a poisoned dataset with mismatched text/audio pairs following the same steps as presented in the paper (basically choosing two unrelated concepts: A, C, building a collection of text prompts containing the word A and building a collection of audios where each file captures the essence of C). Having such dataset, we want to fine tune the AudioLDM model using this [repo](https://github.com/haoheliu/AudioLDM-training-finetuning) which has already been added as a git submodule. Our progress in this field can be seen in this [notebook](https://github.com/WIMU-BKT/WIMU-Data-poisoning/blob/audioldm-finetuning/wimudp/data-poisoning/finetuning_notebook.ipynb). This notebook is already done and it allows us to conduct the dirty label attack step-by-step (we already solved the problem with vRAM usage). Although, we are still testing which hyperparameters are most suitable and whether audios from AudioCaps dataset (which are downloaded via this [script](https://github.com/WIMU-BKT/WIMU-Data-poisoning/blob/audioldm-finetuning/wimudp/data_poisoning/dirty_label/audio_loader.py)) or audios generated by clean AudioLDM model based AudioCaps captions are the best.
### Nightshade
Our next aim is to reproduce the Nightshade attack following the three steps shown by authors in section 5.3 (Detailed Attack Design) which include: selecting poison text prompts, generating anchor images and constructing poison images. We've already done the research and prepared detailed explanation of our approach:
- firstly, we want to use the pretraiend CLAP model which the text encoder for AudioLDM model (section 1 in [AudioLDM paper](https://arxiv.org/pdf/2301.12503)) to calculate cosine similarity between each caption from AudioCaps dataset and targeted concept (concept C). From top ranked captions we want to randomly choose N prompts
- then, based on selected text prompts, we are going to query clean AudioLDM to generate N audio samples connected to another concept (concept A) which is unrelated to concept C
- in the third step, we want to use backpropagation to find minimum value of: min|F(x_c + *d*), F(x_a)| with respect to *d* where F is the feature extractor - VAE (section in [AudioLDM paper](https://arxiv.org/pdf/2301.12503)), || is the distance in the semantic space and x_c and x_a are MEL-spectrograms of original audio sample (connected to specific text prompt) and generated audio sample (generated in step 2). Having the optimal value of *d*, we can perturbate the original image by adding some value to MEL-spectrogram and create waveform using vocoder.
### Results
We focused on Nightshad attack results. We wanted model to confuse cat meowing with dog barking. In order to do this we generated around 180 poison samples and compared clean pretrained model output with poisoned model output for prompt "Cat meows":


https://github.com/user-attachments/assets/d12e13cf-c677-433f-b659-1cb1f70c3325

Audio from clean pretrained AudioLDM - CLAP metric comparing prompt to audio: 0.35.


https://github.com/user-attachments/assets/78dde08b-a442-4b63-a1fb-bd48a01def5e

Audio from poisoned AudioLDM - CLAP metric comparing prompt to audio: 0.20.


## Bibliography
- AudioSeal: https://arxiv.org/abs/2401.17264v2 / https://github.com/facebookresearch/audioseal/tree/main
- VampNet: https://arxiv.org/abs/2307.04686 / https://github.com/hugofloresgarcia/vampnet
- MusicGen: https://arxiv.org/abs/2306.05284 / https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md
- SampleRNN: https://arxiv.org/abs/1612.07837 / https://github.com/soroushmehr/sampleRNN_ICLR2017/tree/master
- Nightshade: https://arxiv.org/pdf/2310.13828
- Glaze: https://www.usenix.org/system/files/usenixsecurity23-shan.pdf
- SilentBadDiffusion: https://arxiv.org/abs/2401.04136 / https://github.com/haonan3/SilentBadDiffusion
