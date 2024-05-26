import numpy as np
import matplotlib.pyplot as plt

# Função para calcular raízes de polinômios e plotar o diagrama de polos e zeros
def plot_pole_zero(zeros, poles, title):
    # Calcula os zeros e polos
    
    # Configuração do gráfico
    plt.figure(figsize=(8, 8))
    plt.scatter(zeros.real, zeros.imag, marker='o', s=100, facecolors='none', edgecolors='b', label='Zeros')
    plt.scatter(poles.real, poles.imag, marker='x', s=100, color='r', label='Polos')
    plt.axhline(0, color='gray', lw=1)
    plt.axvline(0, color='gray', lw=1)
    plt.xlabel('Real')
    plt.ylabel('Imaginário')
    plt.title(title)
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# Plotando os diagramas
zeros = np.array([0.5])
poles = np.array([0.98, 0.95])
plot_pole_zero(zeros, poles, "")
plot_pole_zero(poles, zeros, "")