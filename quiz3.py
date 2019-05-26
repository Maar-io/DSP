import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"""
N = 120
n = np.arange(N)
fo1 =12/120
fo2 = 6/120
x1=np.cos(2*np.pi*fo1*n) + np.cos(2*np.pi*fo2*n)
X1 = np.fft.fft(x1)
plt.stem(n, abs(X1))
plt.show()
"""


#quiz 4.10

def dft_shift(X):
    N = len(X)
    if (N % 2 == 0):
        # even-length: return N+1 values
        return np.arange(-N/2, N/2 + 1), np.concatenate((X[int(N/2):], X[:int(N/2)+1]))
    else:
        # odd-length: return N values
        return np.arange(-(N-1)/2, (N-1)/2 + 1), np.concatenate((X[(int((N+1)/2)):], X[:(int((N+1)/2))]))




N = 1024
n = np.arange(N)
f1 = N/8
x = np.cos(2*np.pi/N *f1 *n)
plt.stem(n, x)
plt.show()
X = np.fft.fft(x)
xos, y = dft_shift(X)
plt.stem(xos, abs(y))
plt.show()


