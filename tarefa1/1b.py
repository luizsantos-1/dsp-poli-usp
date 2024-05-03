import numpy as np

# Função para calcular e imprimir polos ordenados por módulo e seus módulos
def print_sorted_poles(numerator, denominator, title):
    # Calcula os polos
    poles = np.roots(denominator)
    # Ordena os polos por módulo
    sorted_poles = sorted(poles, key=lambda x: np.abs(x))
    # Imprime os polos ordenados com seus módulos
    print(f"Polos ordenados por módulo para {title}:")
    for pole in sorted_poles:
        modulus = np.abs(pole)
        print(f"Polo: {pole:.4f} | Módulo: {modulus:.4f}")

# Coeficientes dos polinômios para X_0(z), X_1(z) e X_2(z)
num0 = [1, -3, 2]
den0 = [1, -2, 3/4]

num1 = [1.7, 1, 0.7]
den1 = [1, -1.2, 0.8]

num2 = [4, -8.68, -17.98, 26.74, -8.04]
den2 = [1, -2, 10.2, 6, 65]

# Imprime os polos ordenados para cada função
print_sorted_poles(num0, den0, 'X_0(z)')
print_sorted_poles(num1, den1, 'X_1(z)')
print_sorted_poles(num2, den2, 'X_2(z)')
