# Requirements:
# Python >= 3.8
# Pytorch >= 1.13.0
# Omegaconf
# Julius
# Numpy
# pip install audioseal

from audioseal import AudioSeal
model = AudioSeal.load_generator("audioseal_wm_16bits")
