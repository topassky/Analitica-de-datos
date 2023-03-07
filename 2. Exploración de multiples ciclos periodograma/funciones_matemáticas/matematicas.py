import numpy as np

# Funciones para calcular el seno y coseno
def seno(fs, t):
    return np.sin(((2 * np.pi)/fs) * t)

def coseno(fs, t):
    return np.cos(((2 * np.pi)/fs) * t)