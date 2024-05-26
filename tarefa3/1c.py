import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, lfilter
from scipy.fft import fft, fftfreq, fftshift
from scipy.io import wavfile

# Read the .wav file
sample_rate, x = wavfile.read('Que_maravilha_cut.wav')

# Parameters
N = len(x)

# Distortion filter
A = convolve([1, -0.95], [1, -0.98])
B = [1, -0.5]  # or B = [1, -2]

# Compensator filter (complete these values as needed)
Ac = [1, -0.5]  # Example values
Bc = convolve([1, -0.95], [1, -0.98])  # Example values

# Corrupted signal
y = lfilter(B, A, x)

# Recovered signal
x_est = lfilter(Bc, Ac, y)

# FFT calculation
X = fft(x)
X_est = fft(x_est)
Y = fft(y)

# Use only the first 1000 samples for plotting
num_samples = 100000
x_plot = x[:num_samples]
x_est_plot = x_est[:num_samples]
freqs_plot = fftfreq(num_samples, 1/sample_rate)

# Plotting the signals
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Time domain plots
axes[0, 0].plot(x_plot[:, 0], label='Original Signal (x)', linewidth=0.5)
axes[0, 0].legend()
axes[0, 0].set_title('Sinal original no domínio do tempo')

axes[0, 1].plot(x_est_plot[:, 0], label='Recovered Signal (x_est)', color='orange', linewidth=0.5)
axes[0, 1].legend()
axes[0, 1].set_title('Sinal recuperado no domínio do tempo')

# Magnitude of FFT
axes[1, 0].plot(fftshift(freqs_plot), fftshift(np.abs(X[:num_samples]))[:, 0], label='Magnitude of X', linewidth=0.5)
axes[1, 0].legend()
axes[1, 0].set_title('Magnitude da representação em frequência do sinal original')

axes[1, 1].plot(fftshift(freqs_plot), fftshift(np.abs(X_est[:num_samples]))[:, 0], label='Magnitude of X_est', color='orange', linewidth=0.5)
axes[1, 1].legend()
axes[1, 1].set_title('Magnitude da representação em frequência do sinal recuperado')

plt.tight_layout()
plt.show()

# Save the recovered signal as .wav file
wavfile.write('Recovered_Que_maravilha_cut.wav', sample_rate, np.asarray(x_est, dtype=np.int16))
wavfile.write('Distorted_Que_maravilha_cut.wav', sample_rate, np.asarray(y, dtype=np.int16))
