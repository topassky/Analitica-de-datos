# Importar las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo de datos y guardar la información en un DataFrame
df = pd.read_csv('base_datos/lluviaSC.dat', header=None, delim_whitespace=True)

# Selecciona las columnas con índices 2, 4, 6 y 8
df_n = df.iloc[:, [2, 4, 6, 8]]

# Crear una lista de listas vacías para almacenar los valores de la variable en los instantes temporales t = 25,50,75 y 100
instantes = [[],[],[],[]]

# Recorrer la lista de muestras generadas
for i in df_n.values:
    # Almacenar el valor de la variable en el instante temporal t = 2
    instantes[0].append(i[0])
    # Almacenar el valor de la variable en el instante temporal t = 4
    instantes[1].append(i[1])
    # Almacenar el valor de la variable en el instante temporal t = 6
    instantes[2].append(i[2])
    # Almacenar el valor de la variable en el instante temporal t = 8
    instantes[3].append(i[3])

# Crear una figura con varios subplots
fig, axs = plt.subplots(2, 2, figsize=(5, 5))

# Crear una lista de colores
colors = ['blue', 'red', 'green', 'purple']

# Crear un ciclo para crear el histograma de distribución para cada arreglo
for i, array in enumerate(instantes):
    axs[i//2, i%2].hist(array, bins=10, density=True, color=colors[i], alpha=0.7, edgecolor='black', linewidth=1.5)
    axs[i//2, i%2].set_xlabel("Valor")
    axs[i//2, i%2].set_ylabel("Frecuencia")
    axs[i//2, i%2].set_title(f"Histograma de distribución {i+1}")

# Mostrar la figura con los subplots
plt.show()


