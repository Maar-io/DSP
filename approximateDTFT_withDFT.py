# https://dspillustrations.com/pages/posts/misc/approximating-the-fourier-transform-with-dft.html

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

def cft(g, f):
    """Numerically evaluate the Fourier Transform of g for the given frequencies"""    
    result = np.zeros(len(f), dtype=complex)
    
    # Loop over all frequencies and calculate integral value
    for i, ff in enumerate(f):
        # Evaluate the Fourier Integral for a single frequency ff, 
        # assuming the function is time-limited to abs(t)<5
        result[i] = complex_quad(lambda t: g(t)*np.exp(-2j*np.pi*ff*t), -5, 5)
    return result

def complex_quad(g, a, b):
    """Return definite integral of complex-valued g from a to b, 
    using Simpson's rule"""
    # 2501: Amount of used samples for the trapezoidal rule
    t = np.linspace(a, b, 2501)  
    x = g(t)
    return integrate.simps(y=x, x=t) # Use Simpson's rule to compute integral from samples.

"""
Let us assert the correctness of this function by checking the Fourier Transform of the rectangular window, 
where we know the correspondence

F{rect(t)} = sin(πf) / πf.

"""
def rect(t):
    return (abs(t) < 0.5).astype(float)

t = np.linspace(-2,2, 1000)

plt.subplot(121)
plt.plot(t, rect(t))

f = np.linspace(-5, 5, 1000)
R = cft(rect, f)  # Calculate the numeric Fourier Transform of the rect function

plt.subplot(122)
plt.plot(f, R.real, 'r-', lw=2, label='Numeric real')
plt.plot(f, R.imag, 'r--', label='Numeric imag')
plt.plot(f, np.sin(np.pi*f)/(np.pi*f), 'k--', lw=5, label='Analytic')
plt.show()


