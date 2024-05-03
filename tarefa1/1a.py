import numpy as np
import matplotlib.pyplot as plt

# Função para calcular raízes de polinômios e plotar o diagrama de polos e zeros
def plot_pole_zero(numerator, denominator, title):
    # Calcula os zeros e polos
    zeros = np.roots(numerator)
    poles = np.roots(denominator)
    
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

# Coeficientes dos polinômios para X_0(z), X_1(z) e X_2(z)
num0 = [1, -3, 2]
den0 = [1, -2, 3/4]

num1 = [1.7, 1, 0.7]
den1 = [1, -1.2, 0.8]

num2 = [4, -8.68, -17.98, 26.74, -8.04]
den2 = [1, -2, 10.2, 6, 65]

# Plotando os diagramas
plot_pole_zero(num0, den0, 'Diagrama de Polos e Zeros para X_0(z)')
plot_pole_zero(num1, den1, 'Diagrama de Polos e Zeros para X_1(z)')
plot_pole_zero(num2, den2, 'Diagrama de Polos e Zeros para X_2(z)')
