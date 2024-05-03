import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

# Load the MATLAB file
data = sio.loadmat('dados05102012.mat')

# Extract the signals
ecg2 = data['ecg2'].squeeze()  # Use squeeze to remove singleton dimensions
sinal = data['sinal'].squeeze()

# Compute the Fourier Transform
fft_ecg2 = np.fft.fft(ecg2)
fft_sinal = np.fft.fft(sinal)

# Compute the frequency axis
n = len(ecg2)  # Number of points in the signal
frequency = np.fft.fftfreq(n, d=1/1200)  # Assuming sampling rate is 1 Hz, replace '1' with actual rate if different

# Define frequency limits
freq_min = -400
freq_max = 400

# Find indices where the frequency is within the desired range
indices = (frequency >= freq_min) & (frequency <= freq_max)

# Plotting the magnitude of the FFT for both signals within the restricted frequency range
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(frequency[indices], np.abs(fft_ecg2)[indices])
plt.title('Fourier Transform of ECG2')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(freq_min, freq_max)

plt.subplot(1, 2, 2)
plt.plot(frequency[indices], np.abs(fft_sinal)[indices])
plt.title('Fourier Transform of Sinal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(freq_min, freq_max)

plt.tight_layout()
plt.show()
