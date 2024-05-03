import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Defining the variables
fa = 1200  # Sampling frequency
fint = 60  # Fundamental frequency to be eliminated
K = 5  # Fundamental plus K-1 harmonics

# Calculate the zeros of the transfer function
omega0 = 2 * np.pi * fint / fa
z1 = np.exp(1j * omega0 * np.arange(1, K+1))

# Adding complex conjugates to maintain real coefficients
z2 = np.conjugate(z1)
zz = np.concatenate([z1, z2])  # Combine all zeros

# Calculate poles with the same phase but 95% of the magnitude
pp = 0.95 * zz

# Convert zeros to polynomial coefficients for the numerator of the FIR filter
bfir = Polynomial.fromroots(zz).coef
bfir_rounded = np.round(bfir, 2)

# Convert poles to polynomial coefficients for the denominator
bden = Polynomial.fromroots(pp).coef
bden_rounded = np.round(bden, 2)

# Printing the rounded coefficients
print("IIR filter numerator coefficients (rounded):", bfir_rounded)
print("IIR filter denominator coefficients (rounded):", bden_rounded)

# Plotting the zero-pole diagram
plt.figure(figsize=(8, 8))
plt.plot(np.real(zz), np.imag(zz), 'bo', label='Zeros')
plt.plot(np.real(pp), np.imag(pp), 'rx', label='Poles', markersize=10)
plt.title('Zero-Pole Diagram of IIR')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
