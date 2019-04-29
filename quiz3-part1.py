import matplotlib
import matplotlib.pyplot as plt
import numpy as np


"""
print("------------------quiz3.4.a-------------")
x = np.arange(1,6)
print("x = ", x)
X = np.fft.fft(x)
print("DFT(x) =", X)
y = np.fft.fft(X)
print("DTF(DTF(x)) =", y)
plt.stem(abs(y))
plt.show()

print("------------------quiz3.4.b-------------")
x = np.array([1,-1, 1, -1, 1, -1])
print("x = ", x)
X = np.fft.fft(x)
print("coef X=", X)
plt.stem(abs(X))
plt.show()

print("------------------quiz3.4---------------")
N = 64
n = np.arange(N)
y1 = 2 * np.cos(4 * 2 * np.pi * n / N)
y2 = 0.5 * np.sin(8 * 2 * np.pi * n / N)
y3 = np.ones((64,), dtype=int)
x = y1 + y2 + y3 
plt.plot(n, y1)
plt.plot(n, y2)
plt.plot(n, y3)
plt.plot(n, x)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.show()

print("------------------quiz3.6---------------")
Y3 = np.fft.fft(y3)
plt.stem(n, abs(Y3))
plt.show()
print("Y3[0], otherwise Y3[1]", Y3[0], Y3[1])

Y1 = np.fft.fft(y1)
plt.stem(n, abs(Y1))
plt.show()
print("otherwise Y1[0], Y1[4], Y1[60]", Y1[0], Y1[4], Y1[60])

Y2 = np.fft.fft(y2)
plt.stem(n, Y2)
plt.show()
print("otherwise Y2[0], Y2[8], Y2[56]", Y2[0], Y2[4], Y2[60])

X = np.fft.fft(x)
x_norm = np.linalg.norm(x)
x2_norm = np.linalg.norm(x[2])
print(X[2], x_norm, x2_norm )

"""
print("------------------quiz3.7---------------")
L=12
N=64
n = np.arange(N)
z = np.cos(2 * np.pi * n * L/N)
Z = np.fft.fft(z)
plt.stem(n, Z)
plt.show()
for i in n:
    print(i, Z[i])

