import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Definindo os coeficientes das funções de transferência
# Ha(z)
num_a = [1, -1.2, 1]
den_a = [1]

# Hb(z)
num_b = [1]
den_b = [1, -1.2, 0.95]

# Calculando a resposta em frequência
w_a, h_a = freqz(num_a, den_a)
w_b, h_b = freqz(num_b, den_b)

# Convertendo frequências de rad/sample para Hz
fs = 8000  # frequência de amostragem
frequencies_a = w_a * fs / (2 * np.pi)
frequencies_b = w_b * fs / (2 * np.pi)

# Plotando a magnitude e a fase para Ha(z)
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
plt.plot(frequencies_a, 20 * np.log10(abs(h_a)), label='Magnitude')
plt.title('Resposta em Magnitude de Ha(z)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(frequencies_a, np.angle(h_a) * 180 / np.pi, label='Fase')
plt.title('Resposta de Fase de Ha(z)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Plotando a magnitude e a fase para Hb(z)
plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
plt.plot(frequencies_b, 20 * np.log10(abs(h_b)), label='Magnitude')
plt.title('Resposta em Magnitude de Hb(z)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(frequencies_b, np.angle(h_b) * 180 / np.pi, label='Fase')
plt.title('Resposta de Fase de Hb(z)')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (graus)')
plt.grid(True)

plt.tight_layout()
plt.show()
