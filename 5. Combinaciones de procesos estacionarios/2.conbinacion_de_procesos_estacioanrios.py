import numpy as np
from scipy.linalg import toeplitz

def calcular_autocovarianza(datos, retardo):
    n = len(datos)
    media = np.mean(datos)
    autocovarianza = 0
    
    for t in range(n - retardo):
        autocovarianza += (datos[t] - media) * (datos[t - retardo] - media)
        
    autocovarianza /= (n - retardo)
    return autocovarianza

# Ejemplo de uso
n_samples = 1000
z1 = np.random.normal(0, 1, n_samples)
z2 = np.roll(z1, 1)
z3 = np.roll(z1, 2)

# Combinación lineal de z1, z2 y z3
yt = 0.5 * z1 + 0.3 * z2 + 0.2 * z3

retardos = [0, 1, 2, 3]

autocovarianzas = [calcular_autocovarianza(yt, retardo) for retardo in retardos]

toeplitz_matrix = toeplitz(autocovarianzas)

print(toeplitz_matrix)
