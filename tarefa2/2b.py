import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, ZerosPolesGain, dfreqresp

def plot_filter_response(gain):
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
    z2 = z2[np.abs(np.real(z2) + 1) > 1e-10]

    # Combinando todos os zeros e garantindo que não elimine a componente DC
    zz = np.concatenate([z1, z2])

    # Criando o sistema com o ganho especificado
    system = ZerosPolesGain(zz, np.array([]), gain, dt=1/fa)
    function = system.to_tf()
    frequencias, resposta = dfreqresp(function)
    frequencias = frequencias * fa

    # Convertendo a resposta em dB
    magnitude_dB = 20 * np.log10(np.abs(resposta))

    # Plotando a resposta em frequência (magnitude)
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(frequencias / (2*np.pi), magnitude_dB)
    plt.title(f'Resposta em Frequência do Filtro FIR com Ganho {gain}')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid(True)

    # Plotando a fase da resposta em frequência
    plt.subplot(2, 1, 2)
    fase = np.unwrap(np.angle(resposta))
    plt.plot(frequencias / (2*np.pi), fase)
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Fase (Radianos)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Chamar a função para ganho de 1 e depois para ganho de 12
plot_filter_response(1)
plot_filter_response(12)
