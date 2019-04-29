import matplotlib
import matplotlib.pyplot as plt
import numpy as np

N = 128
n = np.arange(N)
fo1 = 21/128
x1=np.cos(2*np.pi*fo1*n)
fo2 = 21/127
x2=np.cos(2*np.pi*fo2*n)

X1 = np.fft.fft(x1)
plt.stem(n, abs(X1))
plt.show()

X2 = np.fft.fft(x2)
plt.stem(n, abs(X2))
plt.show()