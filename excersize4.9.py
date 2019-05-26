import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cmath

np.seterr(divide='ignore', invalid='ignore')
"""
Consider the following infinite non-periodic discrete time signal x[n] =
            0 n < 0,
            1 0 ≤ n < a,
            0 n ≥ a.
(a) Compute its DTFT X(e to jw).
(b) We want to visualize the magnitude of X(e to jw) using Matlab. However,
Matlab can not handle continuous sequences as X(e to jw), thus we need to
consider only a finite number of points. Using Matlab, plot 10000 points
of one period of|X(e to jw)| (from 0 to 2π) for a = 20.
"""

"""
N = 10000 
a= 20
n = np.arange(N)
print(max(n))
w = n * 2*np.pi/max(n)
#print(w)
X = (1-np.exp(-1j *a *w)) / (1 - np.exp(-1j *w))
#print(X)
plt.stem(n, abs(X))
plt.show()
"""
"""
(c) The DTFT is mostly a theoretical analysis tool, but in many cases, we
will compute the DFT. Recall that in Matlab we use the Fast Fourier
Transform (FFT), an efficient algorithm to compute the DFT. Generate
a finite sequence x1[n] of length N = 30 such that x1[n] = x[n] for n =
1, . . . , N. Compute its DFT and plot itsmagnitude. Compare it with the
plot obtained in (b).
"""

N = 1000 # repeat for diff values 50, 100, 1000
a = 20
n = np.arange(N)
x = np.array(np.ones(a))
#print("x=", x)
x = np.append(x, np.zeros(N-a))
#print("x2=", x)
X = np.fft.fft(x)
plt.stem(n, abs(X))
plt.show()

"""
The DFT of x[n] for various values of N is represented in Figure 3.4.
As we increase N, the DFT becomes closer and closer to the DTFT of
x[n]. We know that the DFT and the DFS are formally identical, and
as N grows, the DFS converges to the DTFT. We can use Matlab to
approximate the DTFT of any signal.
"""