from calculo_estacionalidad.parametros_estacionalidad import Parametros_Estacionalidad
from funciones_matemáticas.matematicas import seno, coseno
import numpy as np

class Funcion_Periodica_Como_Suma_De_Ondas_Asociadas:
    def __init__(self, data ,fs_data, t):
        self.data = data
        self.fs_data = fs_data
        self.t = t
    
    def calculo (self):
        # Calcular los parámetros A y B para cada frecuencia en fs_data_new
        contantes_A = []
        contantes_B = []
        for fs in self.fs_data:
            # Calcular la frecuencia angular
            w = 2*np.pi*fs
            # Crear un objeto de clase Parametros_Estacionalidad
            parametro = Parametros_Estacionalidad(self.data, w, self.t)
            # Calcular el parámetro A y B para la frecuencia actual
            A = parametro.calculo_parametro_A()
            B = parametro.calculo_parametro_B()
            # Agregar los valores de A y B a las listas correspondientes
            contantes_A.append(A)
            contantes_B.append(B)

        # Inicializar una lista para almacenar los valores totales
        y_total = np.zeros(len(self.t))
        # Sumar las contribuciones de cada frecuencia
        for A, B, fs in zip(contantes_A, contantes_B, self.fs_data):
            y = A*seno(fs, self.t) + B*coseno(fs, self.t)
            for i in range(len(y)):
                y_total[i] = y_total[i]+y[i]

        # Añadir el valor medio a la señal total
        y = self.data.mean() + y_total

        return y