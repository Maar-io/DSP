import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cmath

np.seterr(divide='ignore', invalid='ignore')

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