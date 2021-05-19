from dtw import dtw
import matplotlib.pyplot as plt
import numpy as np
import librosa
import IPython.display
import os
from IPython.display import Image


# filename = librosa.ex('trumpet')
cwd=os.getcwd()
print(cwd)
path=os.path.join(cwd,"audio_file","J&Tmaaf.ogg")
path2=os.path.join(cwd,"audio_file","j&t.ogg")
print(cwd)
def read_audio(audio):
  x, fs = librosa.load(audio, sr=None)
  return x,fs

x,fs=read_audio(path)
y,fs1=read_audio(path2)
plt.plot(x)
IPython.display.Audio(data=x, rate=fs)
plt.show()

