# Importar las librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo de datos y guardar la información en un DataFrame
df = pd.read_csv('base_datos/lluviaSC.dat', header=None, delim_whitespace=True)

# Crear un array con los valores de t
t = np.linspace(1, len(df.iloc[0]), num=len(df.iloc[0]))

# Crear una figura con subplots
fig, ax = plt.subplots()

# Establecer el título de la figura
ax.set_title('Series mensuales de las precipitaciones en Madrid durante los años 1988 a 1999.')

# Bucle para dibujar las series mensuales
for i in range (len(df)):
    # Dibujar la i-ésima serie
    ax.plot(t, df.iloc[i], linewidth=2.0)

# Establecer el título del eje x
ax.set_xlabel('Posición de la muestra')

# Establecer el título del eje y
ax.set_ylabel('Serie')

# Mostrar la malla en el gráfico
ax.grid(True)

# Mostrar la figura con los subplots
plt.show()
