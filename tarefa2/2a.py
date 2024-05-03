import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Definindo as variáveis
fa = 1200  # frequência de amostragem
fint = 60  # frequência fundamental a ser eliminada
K = 5  # fundamental mais K-1 harmônicas

# Cálculo dos zeros da função de transferência
omega0 = 2 * np.pi * fint / fa
z1 = np.exp(1j * omega0 * np.arange(1, K+1))

# Adicionando os complexos conjugados para manter os coeficientes reais
z2 = np.conjugate(z1)
# Removendo zeros em -1 para evitar duplicidade (considerando um limite pequeno para comparar valores flutuantes)
#z2 = z2[np.abs(np.real(z2) + 1) > 1e-10]

# Combinando todos os zeros e garantindo que não elimine a componente DC
zz = np.concatenate([z1, z2])

# Convertendo os zeros em coeficientes do polinômio para o numerador do filtro FIR
bfir = Polynomial.fromroots(zz).coef
bfir_rounded = np.round(bfir, 2)

# Imprimindo os coeficientes arredondados
print("Coeficientes do filtro FIR arredondados:", bfir_rounded)

# Plotagem do diagrama de zeros
plt.figure(figsize=(8, 8))
plt.plot(np.real(zz), np.imag(zz), 'bo', label='Zeros')
plt.title('Zeros do FIR')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
