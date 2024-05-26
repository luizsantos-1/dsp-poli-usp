import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, lfilter
from scipy.fft import fft, fftfreq, fftshift

# Parameters
N = 100
x = (0.8) ** np.arange(N)

# Distortion filter
A = [1, -2]
B = convolve([1, -0.98], [1, -0.95])  # or B = [1, -2]

# Compensator filter (complete these values as needed)
Ac = convolve([1, -0.95], [1, -0.98])  # Example values
Bc = [1, -0.5]  # Example values

# Corrupted signal
y = lfilter(A, B, x)

# Recovered signal
x_est = lfilter(Ac, Bc, y)

# FFT calculation
X = fft(x)
X_est = fft(x_est)
Y = fft(y)

# Frequency axis
freqs = fftfreq(N)

# Plotting the signals
fig, axes = plt.subplots(3, 2, figsize=(10, 7))

# Time domain plots
axes[0, 0].plot(x, label='Sinal original (x)')
axes[0, 0].legend()
axes[0, 1].plot(x_est, label='Sinal recuperado (x_est)', color='orange')
axes[0, 1].legend()

# Magnitude of FFT
axes[1, 0].plot(fftshift(freqs), fftshift(np.abs(X)), label='Magnitude de X')
axes[1, 0].legend()
axes[1, 1].plot(fftshift(freqs), fftshift(np.abs(X_est)), label='Magnitude de X_est', color='orange')
axes[1, 1].legend()

# Phase of FFT
axes[2, 0].plot(fftshift(freqs), fftshift(np.angle(X)), label='Fase de X')
axes[2, 0].legend()
axes[2, 1].plot(fftshift(freqs), fftshift(np.angle(X_est)), label='Fase de X_est', color='orange')
axes[2, 1].legend()

plt.tight_layout()
plt.savefig('1b.png')  # Save the figure as an image file
plt.show()
