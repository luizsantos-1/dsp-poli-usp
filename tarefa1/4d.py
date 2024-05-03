import numpy as np
from scipy.signal import lfilter
import matplotlib.pyplot as plt

# Sample signal
n = np.arange(1000)
x = np.cos(3 * np.pi * n / 4)

# Define r0 and theta combinations
r0_theta_values = [
    (0.98, 0), (0.98, np.pi/4), (0.98, np.pi/2), (0.98, np.pi),
    (0.15, 0), (0.15, np.pi/4), (0.15, np.pi/2), (0.15, np.pi)
]

# Create a dictionary to store filtered signals by r0
filtered_signals = {}

# Loop over r0 and theta values
for r0, theta in r0_theta_values:
    # Calculate filter coefficients
    b = [1]  # Numerator coefficients (FIR part)
    a = [1, -2 * r0 * np.cos(theta), r0**2]  # Denominator coefficients (IIR part)

    # Filter the signal
    y = lfilter(b, a, x)

    # Store filtered signals grouped by r0 and theta
    filtered_signals[(r0, theta)] = y

# Create the first subplot figure for the first four filters
fig1, axes1 = plt.subplots(4, 1, figsize=(7, 10))  # 4 rows, 1 column
fig1.subplots_adjust(hspace=0.5)  # Space between subplots
fig1.suptitle('Signal Filtering Comparison: Set 1', fontsize=16)

# Plotting the first four filters
for idx, key in enumerate(list(filtered_signals.keys())[:4]):
    ax = axes1[idx]
    ax.stem(n[975:], filtered_signals[key][975:], linefmt='r', markerfmt='ro', basefmt=" ")
    ax.set_title(f'Filter Settings: $r_0 = {key[0]:.2f}, \\theta = {key[1]:.2f}$')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

# Save the first figure
fig1.savefig('filtered_signals_comparison_set1.png', dpi=300)

# Create the second subplot figure for the remaining four filters
fig2, axes2 = plt.subplots(4, 1, figsize=(7, 10))  # 4 rows, 1 column
fig2.subplots_adjust(hspace=0.5)  # Space between subplots
fig2.suptitle('Signal Filtering Comparison: Set 2', fontsize=16)

# Plotting the remaining four filters
for idx, key in enumerate(list(filtered_signals.keys())[4:]):
    ax = axes2[idx]
    ax.stem(n[975:], filtered_signals[key][975:], linefmt='r', markerfmt='ro', basefmt=" ")
    ax.set_title(f'Filter Settings: $r_0 = {key[0]:.2f}, \\theta = {key[1]:.2f}$')
    ax.set_ylabel('Amplitude')
    ax.grid(True)

# Save the second figure
fig2.savefig('filtered_signals_comparison_set2.png', dpi=300)

# Show both plots
plt.show()
