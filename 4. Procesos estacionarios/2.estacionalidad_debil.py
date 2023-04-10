import numpy as np

def calcular_autocovarianza(datos, retardo):
    n = len(datos)
    media = np.mean(datos)
    autocovarianza = 0
    
    for t in range(n - retardo):
        autocovarianza += (datos[t] - media) * (datos[t - retardo] - media)
        
    autocovarianza /= (n - retardo)
    return autocovarianza

def verificar_estacionalidad_debil(datos, num_segmentos, retardos):
    n = len(datos)
    segmento_len = n // num_segmentos
    
    # Calcular medias y varianzas de los segmentos
    medias = [np.mean(datos[i * segmento_len:(i + 1) * segmento_len]) for i in range(num_segmentos)]
    varianzas = [np.var(datos[i * segmento_len:(i + 1) * segmento_len]) for i in range(num_segmentos)]

    # Calcular autocovarianzas para diferentes retardos
    autocovarianzas = [calcular_autocovarianza(datos, retardo) for retardo in retardos]

    # Verificar si las medias y varianzas son similares en todos los segmentos
    tolerancia = 1
    media_similar = np.max(medias) - np.min(medias) < tolerancia
    varianza_similar = np.max(varianzas) - np.min(varianzas) < tolerancia

    return media_similar, varianza_similar, autocovarianzas

# Ejemplo de uso
datos = np.random.normal(0, 1, 1000)  # Serie de tiempo
num_segmentos = 4
retardos = [1,5,10,15,20]

media_similar, varianza_similar, autocovarianzas = verificar_estacionalidad_debil(datos, num_segmentos, retardos)
print("Media similar:", media_similar)
print("Varianza similar:", varianza_similar)
print("Autocovarianzas:", autocovarianzas)

