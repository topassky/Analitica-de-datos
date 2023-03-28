import random
import numpy as np
import matplotlib.pyplot as plt

# Generar un valor aleatorio siguiendo una distribución normal con media 0 y desviación estándar 1
a_t = random.normalvariate(0, 1)

# Inicializar una lista para almacenar conjuntos de muestras
conjunto_muestras = []
# Inicializar un contador para el número de conjuntos de muestras
contador_muestras = 0

# Bucle para generar 200 conjuntos de muestras
while (contador_muestras < 200):
    # Inicializar un arreglo para almacenar las muestras
    muestras = np.zeros(100)
    # Inicializar una variable para almacenar la posición actual
    zt = 0
    # Bucle para generar las muestras
    for i in range (len(muestras)):
        # Generar un valor aleatorio siguiendo una distribución normal con media 0 y desviación estándar 1
        a_t = random.normalvariate(0, 1)
        # Si es la primera muestra, establecerla en 0
        if i == 0:
            muestras[i] = 0
        # Si no es la primera muestra, calcular la posición actual y agregarla al arreglo de muestras
        else:
            ztp = zt + a_t
            muestras[i] = muestras[i]+ztp
            zt = ztp
    # Agregar el conjunto de muestras a la lista
    conjunto_muestras.append(muestras)
    # Incrementar el contador de conjuntos de muestras
    contador_muestras += 1

# Crear una lista de listas vacías para almacenar los valores de la variable en los instantes temporales t = 25,50,75 y 100
instantes = [[],[]]

# Recorrer la lista de muestras generadas
for i in conjunto_muestras:
    # Almacenar el valor de la variable en el instante temporal t = 24
    instantes[0].append(i[23])
    # Almacenar el valor de la variable en el instante temporal t = 25
    instantes[1].append(i[24])


# Calcular la media y la varianza de los datos en instantes 24
media_z_t_24 = np.mean(instantes[0])
varianza = np.var(instantes[0])
varianza_24 = varianza/24

# Calcular la media y la varianza de los datos en instantes 25 
media_z_t_25 = np.mean(instantes[1])
varianza = np.var(instantes[1])
varianza_25 = varianza/25

# Imprimir las medias y las varianzas
print((media_z_t_24, media_z_t_25))
print((varianza_24, varianza_25))

# Crear un subplot con 1 fila y 2 columnas
fig, axs = plt.subplots(1, 2)

# Definir los parámetros para ambos subplots
bins = 10
xlabel = "Valor"
ylabel = "Frecuencia"

# Graficar el instante 0 en el primer subplot
axs[0].hist(instantes[0], bins=bins, density=True, color="blue", alpha=0.7, edgecolor='black', linewidth=1.5)
axs[0].set(title='Histograma de distribución t = 24', xlabel=xlabel, ylabel=ylabel)

# Graficar el instante 1 en el segundo subplot
axs[1].hist(instantes[1], bins=bins, density=True, color="red", alpha=0.7, edgecolor='black', linewidth=1.5)
axs[1].set(title='Histograma de distribución t = 25', xlabel=xlabel, ylabel=ylabel)

# Mostrar el subplot
plt.show()


