import numpy as np
import matplotlib.pyplot as plt

# Definições de parâmetros
r0 = 0.15
theta_values = [0, np.pi/4, np.pi/2, np.pi]
omega = np.linspace(-np.pi, np.pi, 1000)

# Criação de figuras para os gráficos
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Calcular e plotar módulo e fase para cada valor de theta
for theta in theta_values:
    # Calculando a resposta em frequência
    H = 1 / (1 - 2 * r0 * np.cos(theta) * np.exp(-1j*omega) + r0**2 * np.exp(-2j*omega))
    
    # Módulo
    axs[0].plot(omega, np.abs(H), label=f'Theta = {theta:.2f}')
    
    # Fase
    axs[1].plot(omega, np.angle(H), label=f'Theta = {theta:.2f}')

# Configuração dos gráficos
axs[0].set_title('Magnitude of Frequency Response')
axs[0].set_xlabel('Omega (rad/s)')
axs[0].set_ylabel('Magnitude')
axs[0].legend()

axs[1].set_title('Phase of Frequency Response')
axs[1].set_xlabel('Omega (rad/s)')
axs[1].set_ylabel('Phase (radians)')
axs[1].legend()

plt.tight_layout()
plt.show()
