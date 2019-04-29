import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def dft_shift(X):
    N = len(X)
    if (N % 2 == 0):
        # even-length: return N+1 values
        return np.arange(-N/2, N/2 + 1), np.concatenate((X[int(N/2):], X[:int(N/2)+1]))
    else:
        # odd-length: return N values
        return np.arange(-(N-1)/2, (N-1)/2 + 1), np.concatenate((X[(int((N+1)/2)):], X[:(int((N+1)/2))]))


N = 128
n = np.arange(N)
fo1 = 21/128
x1=np.cos(2*np.pi*fo1*n)
fo2 = 21/127
x2=np.cos(2*np.pi*fo2*n)

X1 = np.fft.fft(x1)
n, y = dft_shift(X1)
plt.stem(n, abs(y))
plt.show()

X2 = np.fft.fft(x2)
a, b = dft_shift(X2)
plt.stem(a, abs(b))
plt.show()