import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 3 * np.pi / 4  # Frequency in radians/sample
num_samples = 100          # Number of samples to generate

# Generate sample indices
n = np.arange(num_samples)

# Compute the cosine wave
cosine_wave = np.cos(frequency * n)

# Plotting
plt.figure(figsize=(10, 4))
plt.stem(n, cosine_wave, basefmt=" ")
plt.title('Discrete Time Cosine Wave with Frequency $3\pi/4$ rad/sample')
plt.xlabel('Sample n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
