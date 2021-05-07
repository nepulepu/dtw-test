from dtw import dtw
import matplotlib.pyplot as plt
import numpy as np
import librosa
import IPython.display
import os
from IPython.display import Image

def dtwSound(a1,a2):
  manhattan_distance = lambda a1, a2: np.abs(a1 - a2)
  d, cost_matrix, acc_cost_matrix, path = dtw(a1, a2, dist=manhattan_distance)
  print(d)
  plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
  plt.plot(path[0], path[1], 'w')
  plt.show()

# filename = librosa.ex('trumpet')
cwd=os.getcwd()
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

dtwSound(x, y)