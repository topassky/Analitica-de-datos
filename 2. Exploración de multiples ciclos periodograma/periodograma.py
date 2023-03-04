# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Importar las clases necesarias desde los módulos calculo_multiples_ciclos y calculo_estacionalidad
from calculo_multiples_ciclos.frecuenciasyperiodosbasicos import FrecuenciasYPeriodosBasicos
from calculo_estacionalidad.parametros_estacionalidad import Parametros_Estacionalidad

# Funciones para calcular el seno y coseno
def seno(fs, t):
    return np.sin(((2 * np.pi)/fs) * t)

def coseno(fs, t):
    return np.cos(((2 * np.pi)/fs) * t)

# Leer el archivo de datos y guardar la información en un DataFrame
df = pd.read_csv('base_datos/lluviaSC.dat', header=None, delim_whitespace=True)

# Crear un nuevo DataFrame con una sola columna que contenga los datos de lluvia
new_df = pd.DataFrame(columns=['Data'])
for i in range(df.shape[0]):
    for j in range(df.shape[1]):
        new_df = new_df.append({'Data': df.iloc[i][j]}, ignore_index=True)
new_df = new_df["Data"]

# Calcular las frecuencias básicas
frec_basicas = FrecuenciasYPeriodosBasicos(len(new_df))
fs_data = frec_basicas.calcular_frecuencias()

# Crear una secuencia de tiempo
t = np.linspace(1, len(new_df.index)+1, num=len(new_df.index)+1)

# Calcular los parámetros R
contantes_R = []
for fs in fs_data:
    w = 2*np.pi*fs
    parametro = Parametros_Estacionalidad(new_df, w, t)
    R = parametro.calculo_parametro_R()
    contantes_R.append(R**2)

# Calcular la cantidad de muestras
T = len(new_df)

# Calcular la lista de parámetros originales
original_list = []
for i in contantes_R:
    aux = (T/2)*(i**2)
    original_list.append(aux)

# Ordenar la lista de mayor a menor
sorted_list = sorted(original_list, reverse=True)

# Obtener la posición de cada elemento en la lista original
positions = [i for i, x in enumerate(original_list)]


# Ordenar la lista de posiciones según el orden de la lista ordenada
sorted_positions = [x for _,x in sorted(zip(original_list, positions), reverse=True)]

# Imprimir los resultados
fs_data_new = []
for i in sorted_positions[:len(sorted_positions)-1]:
    fs_data_new.append(fs_data[i])

# Calcular los parámetros A y B para cada frecuencia en fs_data_new
contantes_A = []
contantes_B = []
for fs in fs_data_new:
    # Calcular la frecuencia angular
    w = 2*np.pi*fs
    # Crear un objeto de clase Parametros_Estacionalidad
    parametro = Parametros_Estacionalidad(new_df, w, t)
    # Calcular el parámetro A y B para la frecuencia actual
    A = parametro.calculo_parametro_A()
    B = parametro.calculo_parametro_B()
    # Agregar los valores de A y B a las listas correspondientes
    contantes_A.append(A)
    contantes_B.append(B)

# Inicializar una lista para almacenar los valores totales
y_total = np.zeros(len(t))
# Sumar las contribuciones de cada frecuencia
for A, B, fs in zip(contantes_A, contantes_B, fs_data):
    y = A*seno(fs, t) + B*coseno(fs, t)
    for i in range(len(y)):
        y_total[i] = y_total[i]+y[i]

# Añadir el valor medio a la señal total
y = new_df.mean() + y_total

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
