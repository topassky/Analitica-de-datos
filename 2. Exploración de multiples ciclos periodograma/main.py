# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Importar las clases necesarias desde los módulos calculo_multiples_ciclos y calculo_estacionalidad
from calculo_multiples_ciclos.frecuenciasyperiodosbasicos import FrecuenciasYPeriodosBasicos
from calculo_multiples_ciclos.funcion_periodica_como_suma_de_ondas_asociadas import Funcion_Periodica_Como_Suma_De_Ondas_Asociadas
from calculo_multiples_ciclos.periodograma import Periodograma


# Leer el archivo de datos y guardar la información en un DataFrame
df = pd.read_csv('base_datos/lluviaSC.dat', header=None, delim_whitespace=True)

# Crear un nuevo DataFrame con una sola columna que contenga los datos de lluvia
new_df = pd.DataFrame(columns=['Data'])
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        new_df = new_df.append({'Data': df.iloc[i][j]}, ignore_index=True)
new_df = new_df["Data"]

# Crear una secuencia de tiempo
t = np.linspace(1, len(new_df.index)+1, num=len(new_df.index)+1)

# Calcular las frecuencias básicas
frec_basicas = FrecuenciasYPeriodosBasicos(len(new_df))
fs_data = frec_basicas.calcular_frecuencias()


p = Periodograma(new_df, fs_data, t)
original_list = p.peridograma_calculo()

fs_data_new = p.peridograma_mayor_menor()

y_obj = Funcion_Periodica_Como_Suma_De_Ondas_Asociadas(new_df, fs_data_new, t)
y = y_obj.calculo()

# Crear una figura con dos subplots
fig, ax = plt.subplots(nrows=2, ncols=1)

# Graficar la primera serie de tiempo en el primer subplot
ax[0].plot(new_df, color='blue', linewidth=2, label='Serie de tiempo 1')
# Agregar un título y etiquetas de eje al primer subplot
ax[0].set_title('Grafica de la señal vs Suma de ondas asociadas a todas la frecuencias básicas')
ax[0].set_xlabel('Posición de la muestra')
ax[0].set_ylabel('Serie')
# Agregar una malla al primer subplot
ax[0].grid(True)

# Graficar la segunda serie de tiempo en el segundo subplot
ax[1].plot(y, color='red', linewidth=2, label='Serie de tiempo 2')
ax[1].set_xlabel('Posición de la muestra')
ax[1].set_ylabel('Serie')
# Agregar una malla al segundo subplot
ax[1].grid(True)

# Mostrar la figura con los subplots
plt.show()
