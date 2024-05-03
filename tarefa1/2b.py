import numpy as np
from scipy.signal import freqz
from scipy.optimize import minimize_scalar

def magnitude_response(num, den, w):
    """Calcula a magnitude da resposta em frequência para uma frequência angular específica w."""
    w, h = freqz(num, den, worN=[w])
    return np.abs(h[0])

def optimize_frequency(num, den, fs, opt_type='min'):
    """Otimiza a magnitude da resposta em frequência para encontrar máximos ou mínimos."""
    # Função objetivo para otimização
    def objective(w):
        return magnitude_response(num, den, w) if opt_type == 'min' else -magnitude_response(num, den, w)

    # Intervalo de otimização em radianos por amostra
    res = minimize_scalar(objective, bounds=(0, np.pi), method='bounded')
    frequency_hz = res.x * fs / (2 * np.pi)  # Convertendo para Hz
    return frequency_hz, -res.fun if opt_type == 'max' else res.fun

# Coeficientes dos filtros
num_a = [1, -1.2, 1]
den_a = [1]
num_b = [1]
den_b = [1, -1.2, 0.95]
fs = 8000  # Frequência de amostragem em Hz

# Otimização para Ha(z)
max_freq_a, max_val_a = optimize_frequency(num_a, den_a, fs, 'max')
min_freq_a, min_val_a = optimize_frequency(num_a, den_a, fs, 'min')

# Otimização para Hb(z)
max_freq_b, max_val_b = optimize_frequency(num_b, den_b, fs, 'max')
min_freq_b, min_val_b = optimize_frequency(num_b, den_b, fs, 'min')

print(f"Ha(z) Máximo em {max_freq_a:.2f} Hz com valor {max_val_a:.4f}")
print(f"Ha(z) Mínimo em {min_freq_a:.2f} Hz com valor {min_val_a:.4f}")
print(f"Hb(z) Máximo em {max_freq_b:.2f} Hz com valor {max_val_b:.4f}")
print(f"Hb(z) Mínimo em {min_freq_b:.2f} Hz com valor {min_val_b:.4f}")
