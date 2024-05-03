import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.signal import lfilter, ZerosPolesGain

# Load the MATLAB file
data = sio.loadmat('dados05102012.mat')

# Extract the signals
ecg2 = data['ecg2'].squeeze()  # Use squeeze to remove singleton dimensions
sinal = data['sinal'].squeeze()

# Define the filter
fa = 1200  # sampling frequency in Hz
fint = 60  # fundamental frequency to be eliminated
K = 5  # fundamental plus K-1 harmonics
gain = 1  # Define gain, can be changed as needed

# Compute zeros for the transfer function
omega0 = 2 * np.pi * fint / fa
z1 = np.exp(1j * omega0 * np.arange(1, K+1))
z2 = np.conjugate(z1)
z2 = z2[np.abs(np.real(z2) + 1) > 1e-10]
zz = np.concatenate([z1, z2])
pp = np.array([])  # No poles other than at the origin

# Create ZerosPolesGain system
system = ZerosPolesGain(zz, pp, gain, dt=1/fa)
function = system.to_tf()
a = function.num 
b = function.den # Get the transfer function coefficients

# Filter the signal
filtered_signal = lfilter(a, b, sinal)

# Generate a time array in seconds
t = np.arange(sinal.size) / fa

# Time-Domain Plots
plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(t[1000:], sinal[1000:], label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t[1000:], filtered_signal[1000:], label='Filtered Signal')
plt.title('Filtered Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.savefig('time_domain_signals.png')
plt.show()

# Function to compute FFT and plot
def plot_fft(signal, title, fig, subplot_no):
    fft_data = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal), 1/fa)
    plt.figure(fig)
    plt.subplot(2, 1, subplot_no)
    plt.plot(freq[:len(signal)//2], np.abs(fft_data)[:len(signal)//2])
    plt.title(title)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)

# Frequency-Domain Plots (FFTs)
plot_fft(sinal, 'FFT of Original Signal', 'fft_plots', 1)
plot_fft(filtered_signal, 'FFT of Filtered Signal', 'fft_plots', 2)

plt.tight_layout()
plt.savefig('frequency_domain_signals.png')
plt.show()
