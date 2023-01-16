from calculo_estacionalidad.parametros_estacionalidad import Parametros_Estacionalidad
import numpy as np


class Estacionalidad():
    def __init__ (self, serie_sin_tendencia, tiempo):
        self.serie_sin_tendencia = serie_sin_tendencia
        self.tiempo = tiempo
    
    def calculo(self, periodo):
        media = self.serie_sin_tendencia.mean()
        w = np.pi/periodo 
        parametro = Parametros_Estacionalidad(self.serie_sin_tendencia, w)
        A = parametro.calculo_parametro_A()
        B = parametro.calculo_parametro_B()
        R = parametro.calculo_parametro_R()
        print((A,B,R, media))
        return 0

