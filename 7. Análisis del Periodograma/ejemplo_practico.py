import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definir el número total de observaciones (24 horas de datos, uno por hora)
T = 24

# Generar datos de temperatura simulados con una tendencia diurna y nocturna
np.random.seed(0)  # Para reproducibilidad
horas = np.arange(T)

# Simular un ciclo diario típico: temperaturas más altas durante el día y más bajas durante la noche
# Ajustar la función coseno para reflejar un aumento de temperatura durante el día (aproximadamente de 6 a 18 horas)
temperaturas = 10 * np.sin(2 * np.pi * (horas - 6) / 24) + 20 + np.random.normal(0, 2, T)

# Calcular la Transformada de Fourier de las temperaturas
fft_result = np.fft.fft(temperaturas)

# Calcular las frecuencias asociadas para un ciclo de 24 horas
frequencies = np.fft.fftfreq(T, d=1)

# Calcular el periodograma
periodogram = np.abs(fft_result)**2 / T

# Graficar el periodograma
plt.figure(figsize=(10, 5))
plt.stem(frequencies[:T//2], periodogram[:T//2], use_line_collection=True)  # Solo mostrar frecuencias positivas
plt.title('Periodograma de las temperaturas')
plt.xlabel('Frecuencia (ciclos por hora)')
plt.ylabel('Potencia espectral')
plt.grid(True)
plt.show()

# Mostrar también las temperaturas para visualizar el ciclo diurno/nocturno
plt.figure(figsize=(10, 5))
plt.plot(horas, temperaturas, marker='o')
plt.title('Temperaturas registradas cada hora durante un día')
plt.xlabel('Hora del día')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()
