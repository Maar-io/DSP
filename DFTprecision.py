import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def dft_matrix(N):
    # create a 1xN matrix containing indices 0 to N-1
    a = np.expand_dims(np.arange(N), 0)
    print("a= ", a)
    # take advantage of numpy broadcasting to create the matrix
    W = np.exp(-2j * (np.pi / N) * (a.T * a))
    print("W=", W)
    return W

x = np.array([5, 7, 9])

# DFT matrix
N = len(x)
W = dft_matrix(N)
# DFT
X = np.dot(W, x)
# inverse DFT
x_hat = np.dot(W.T.conjugate(), X) / N

print (x-x_hat)
print("As you can see, the difference between the original vector and the reconstructed vector is not exactly zero")

#
# Numerical errors in phase
# Let's first define a more interesting signal such as a length-128 step signal:

N = 128
x = np.zeros(N)
x[0:64] = 1

#plt.stem(x)

W = dft_matrix(N)

# DFT
X = np.dot(W, x)
#plt.stem(abs(X))
#plt.show()

#plt.stem(np.angle(X))
#plt.show()

"""
Clearly we have a problem with the phase, although the magnitude looks nice. 
This is inherent to the fact that the phase is computed by taking the arctangent of a ratio. 
When the computed DFT values are close to zero, the denominator of the ratio will be also 
close to zero and any numerical error in its value will lead to large errors in the phase. 
As we will see in the next section, this problem can be alleviated by using smarter algorithms than the direct naive method.

Let's still verify the inverse DFT:
"""

x_hat = np.dot(W.T.conjugate(), X) / N

#plt.stem(np.real(x_hat - x))
#plt.show()
#plt.stem(np.imag(x_hat))
#plt.show()
print("Again, the error is very small but clearly not zero.")

# FFT Algorithm

X = np.fft.fft(x)
x_hat = np.fft.ifft(X)

plt.stem(np.angle(X))
plt.show()

plt.stem(np.real(x_hat - x))
plt.show()

plt.stem(np.imag(x_hat))
plt.show()