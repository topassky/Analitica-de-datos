from calculo_estacionalidad.parametros_estacionalidad import Parametros_Estacionalidad
import numpy as np

class Estacionalidad():
    def __init__ (self, serie, tiempo):
        """
        Constructor de la clase Estacionalidad.

        Args:
            serie (array): Serie de tiempo.
            tiempo (array): Vector de tiempo correspondiente a la serie de tiempo.
        """
        self.serie = serie
        self.t = tiempo
    
    def calculo(self, periodo):
        """
        Calcula la estacionalidad de la serie de tiempo.

        Args:
            periodo (int): Período de la estacionalidad.

        Returns:
            array: Serie de tiempo estacional.
        """
        media = self.serie.mean()
        w = 2*np.pi/periodo 
        parametro = Parametros_Estacionalidad(self.serie, w, self.t)
        A = parametro.calculo_parametro_A()
        B = parametro.calculo_parametro_B()
        R = parametro.calculo_parametro_R()
        s_t = np.zeros(len(self.serie))

        for i in range(len(self.serie)):
            s_t[i] = media + A*np.sin(w*self.t[i]) + B*np.cos(w*self.t[i])

        return s_t
