import numpy as np
import pandas as pd

class Nivel_serie():
    def __init__(self, tiempo, serie):
        self.tiempo = tiempo
        self.serie = serie
    
    def calculo(self):
        """
        Función para calcular la tendencia por el método de regresión lineal
        :return: array con la tendencia de la serie temporal
        """
        valor_tiempo_media = self.tiempo.mean()
        tiempo_media_0 = self.tiempo - valor_tiempo_media

        beta_0= self.serie.mean()

        beta_1_num = 0
        beta_1_dem = 0
        for i in range (len(tiempo_media_0)):
            auxzt = (self.serie[i]-beta_0)*tiempo_media_0[i]
            beta_1_num += auxzt
            auxt2 = tiempo_media_0[i] * tiempo_media_0[i]
            beta_1_dem  +=  auxt2

        beta_1 = beta_1_num / beta_1_dem

        tendencia = beta_0 + beta_1*tiempo_media_0
    
        return tendencia


    def caculco_media_movil(self, ventana = 2):
        """
        Función para calcular la tendencia por el método de la media móvil
        :param ventana: tamaño de la ventana para calcular la media móvil
        :return: array con la tendencia de la serie temporal
        """
        tendencia = self.serie.rolling(window = ventana).mean()
        tendencia = tendencia.fillna(method = 'bfill')

        return tendencia