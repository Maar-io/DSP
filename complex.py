import numpy as np
import cmath

z = 2 + 3j

print(z)

"""
Handling complex numbers
angle(z[, deg])	Return the angle of the complex argument.
real(val)	Return the real part of the complex argument.
imag(val)	Return the imaginary part of the complex argument.
conj(x, /[, out, where, casting, order, …])	Return the complex conjugate, element-wise.
"""
r, phi = cmath.polar(z)
print("polar notation", r, phi)

z2 = cmath.rect(r, phi)
print("rect notation", z2)

z3 = r * cmath.exp(phi * 1j)
print("exp notation", z3)

print("pi", cmath.pi)

print("e", cmath.e)