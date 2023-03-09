from calculo_estacionalidad.parametros_estacionalidad import Parametros_Estacionalidad
from scipy.signal import periodogram
import numpy as np
import pandas as pd

class Periodograma():
    def __init__(self, new_df, fs_data, t):
        self.fs_data = fs_data
        self.data = new_df
        self.t = t
    
    def peridograma_calculo(self):
        # Calcular los parámetros R
        contantes_R = []
        for fs in self.fs_data:
            w = 2*np.pi*fs
            parametro = Parametros_Estacionalidad(self.data, w, self.t)
            R = parametro.calculo_parametro_R()
            contantes_R.append(R**2)

        # Calcular la cantidad de muestras
        T = len(self.data)

        # Calcular la lista de parámetros originales
        original_list = []
        for i in contantes_R:
            aux = (T/2)*(i**2)
            original_list.append(aux)
        
        return original_list
    
    def peridograma_mayor_menor(self):

        # Obtener la posición de cada elemento en la lista original
        positions = [i for i, x in enumerate(self.peridograma_calculo())]


        # Ordenar la lista de posiciones según el orden de la lista ordenada
        sorted_positions = [x for _,x in sorted(zip(self.peridograma_calculo(), positions), reverse=True)]

        # Imprimir los resultados
        fs_data_new = []
        for i in sorted_positions:
            fs_data_new.append(self.fs_data[i])
        
        return fs_data_new
    

