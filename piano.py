import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

Fs, x = wavfile.read("piano.wav")


def dft_shift(X):
    N = len(X)
    if (N % 2 == 0):
        # even-length: return N+1 values
        return np.arange(-N/2, N/2 + 1), np.concatenate((X[int(N/2):], X[:int(N/2)+1]))
    else:
        # odd-length: return N values
        return np.arange(-(N-1)/2, (N-1)/2 + 1), np.concatenate((X[(int((N+1)/2)):], X[:(int((N+1)/2))]))
        
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
plt.plot(f, abs(y))