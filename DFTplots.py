import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1.02, 0.02) - 0.5
print("x = ", x)
X = np.fft.fft(x)
#plt.stem(abs(X))
# plt.show()

def dft_shift_old(X):
    N = len(X)
    if (N % 2 == 0):
        # even-length: return N+1 values
        return np.concatenate((X[(N/2):], X[:(N/2)+1]))
    else:
        # odd-length: return N values
        return np.concatenate((X[(int((N+1)/2)):], X[:(int((N-1)/2))]))
# plt.stem(abs(dft_shift(X)))
# plt.show()


# While the function does shift the vector, the indices are still from zero to  N−1 . 
# Let's modify it so that we returs also the proper values for the indices:
def dft_shift(X):
    N = len(X)
    if (N % 2 == 0):
        # even-length: return N+1 values
        return np.arange(-N/2, N/2 + 1), np.concatenate((X[int(N/2):], X[:int(N/2)+1]))
    else:
        # odd-length: return N values
        return np.arange(-(N-1)/2, (N-1)/2 + 1), np.concatenate((X[(int((N+1)/2)):], X[:(int((N+1)/2))]))

n, y = dft_shift(X)
#plt.stem(n, abs(y))
#plt.show()

import scipy
from scipy.io import wavfile
Fs, x = wavfile.read("piano.wav")

def dft_map(X, Fs, shift=True):
    resolution = float(Fs) / len(X)
    if shift:
        n, Y = dft_shift(X)
    else:
        Y = X
        n = np.arange(0, len(Y))
    f = n * resolution
    return f, Y

# let's cut the signal otherwise it's too big
x = x[:32768]
X = np.fft.fft(x)
f, y = dft_map(X, Fs)
#plt.plot(f, abs(y))
#plt.show()

dft_resolution = float(Fs)/ len(x)
print ("DFT resolution is", dft_resolution, "Hz")

# let's search up to 300Hz
max_range = int(300 / dft_resolution)
ix = np.argmax(abs(y[:max_range]))
pitch = f[ix]
print ("the note has a pitch of", pitch, "Hz")

X = np.fft.fft(x)
f, y = dft_map(X, Fs, shift=False)
plt.plot(f[:2000], abs(y[:2000]))
plt.show()