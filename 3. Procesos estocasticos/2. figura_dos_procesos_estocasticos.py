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

# Crear un array con los valores de t
t = np.linspace(1, 100, num=100)

# Crear una figura con subplots
fig, ax = plt.subplots()

# Establecer el título de la figura
ax.set_title('200 muestras aleatorias de tamaño 100 realizadas por un oirdenador')

# Bucle para dibujar las series mensuales
for m in conjunto_muestras:
    # Dibujar la i-ésima serie
    ax.plot(t, m, linewidth=2.0)

# Establecer el título del eje x
ax.set_xlabel('Tiempo')

# Establecer el título del eje y
ax.set_ylabel('Variable')

# Mostrar la malla en el gráfico
ax.grid(True)

# Mostrar la figura con los subplots
plt.show()






