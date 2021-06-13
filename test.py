import numpy as np
import IPython
import os
# We define two sequences x, y as numpy array
# where y is actually a sub-sequence from x
x = np.array([2, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
y = np.array([1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)

from dtw import dtw
audio=os.path.join(os.getcwd(),"audio_file")
IPython.display.Audio(os.path.join(audio,"j&tmaaf.ogg"))
manhattan_distance = lambda x, y: np.abs(x - y)
print (manhattan_distance)
d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)

print(acc_cost_matrix)
# >>> 2.0 # Only the cost for the insertions is kept

# You can also visualise the accumulated cost and the shortest path
import matplotlib.pyplot as plt

plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
plt.plot(path[0], path[1], 'w')
plt.show()