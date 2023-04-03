import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, pearsonr

def generar_proceso_estacionario(media, desviacion, n, autocorrelacion):
    proceso = np.zeros(n)
    proceso[0] = np.random.normal(media, desviacion)
    
    for i in range(1, n):
        proceso[i] = autocorrelacion * proceso[i - 1] + np.random.normal(media, desviacion)
        
    return proceso

def verificar_condiciones(proceso, retardo, tolerancia):
    
    # Distribuciones marginales
    media = np.mean(proceso[:-retardo])
    desviacion = np.std(proceso[:-retardo])
    
    # Coeficientes de asimetría y curtosis
    asimetria = skew(proceso[:-retardo])
    curtosis = kurtosis(proceso[:-retardo])
    
    # Trasladar el proceso en el tiempo
    proceso_trasladado = proceso[retardo:]
    
    # Verificar condiciones
    media_trasladada = np.mean(proceso_trasladado)
    desviacion_trasladada = np.std(proceso_trasladado)
    asimetria_trasladada = skew(proceso_trasladado)
    curtosis_trasladada = kurtosis(proceso_trasladado)

    # Comparar los valores
    condicion_1 = np.abs(media - media_trasladada) < tolerancia
    condicion_2 = np.abs(desviacion - desviacion_trasladada) < tolerancia
    condicion_3 = np.abs(asimetria - asimetria_trasladada) < tolerancia
    condicion_4 = np.abs(curtosis - curtosis_trasladada) < tolerancia

    return condicion_1 and condicion_2 and condicion_3 and condicion_4

def verificar_distribuciones_finito_dimensionales(proceso, retardo):
    correlaciones = []

    correlacion = pearsonr(proceso[:-retardo], proceso[retardo:])
    correlaciones.append(correlacion[0])

    return correlaciones


# Parámetros del proceso estacionario
media = 0
desviacion = 1
n = 1000
autocorrelacion = 0.8
h = 1
tolerancia = 1e-2

# Generar y verificar condiciones
proceso = generar_proceso_estacionario(media, desviacion, n, autocorrelacion)
condiciones_cumplidas = verificar_condiciones(proceso, h, tolerancia)

if (condiciones_cumplidas):
    print(f"Condiciones cumplidas con una tolerancia de {tolerancia}")
else:
    print("Condiciones NO cumplidas")


correlaciones = verificar_distribuciones_finito_dimensionales(proceso, h)

# Imprimir los resultados
print(f"Correlación con retardo {h} es: {correlaciones[0]}")

# Gráfica del proceso
plt.plot(proceso)
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.title("Proceso estocástico estacionario")
plt.show()
