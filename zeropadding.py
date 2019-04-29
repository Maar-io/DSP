import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Let's build a signal with two sinusoids with frequencies more than  Delta  apart and let's look at the spectrum:
N = 256
Delta = 2*np.pi / N
n = np.arange(0, N)

# main frequency (not a multiple of the fundamental freq for the space)
omega = 2*np.pi / 10 

x = np.cos(omega * n) + np.cos((omega + 3*Delta) * n)
#plt.plot(abs(np.fft.fft(x))[:100])
#plt.show()

#Now let's build a signal with two frequencies that are less than Delta apart:
x = np.cos(omega * n) + np.cos((omega + 0.5*Delta) * n)
plt.plot(abs(np.fft.fft(x))[:100])
plt.show()

#  The two frequencies cannot be resolved by the DFT. If you try to increase the
#  data vector by zero padding, the plot will still display just one peak:

xzp = np.concatenate((x, np.zeros(2000)))
#plt.plot(abs(np.fft.fft(xzp))[:500]);