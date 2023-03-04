import numpy as np

class Parametros_Estacionalidad():
    def __init__(self, serie, w, t):
        """
        Inicializa la clase Parametros_Estacionalidad.
        
        Args:
            serie (array-like): la serie temporal.
            w (float): la frecuencia angular de la componente estacional.
            t (array-like): el vector de tiempo.
        """
        self.serie = serie
        self.w = w
        self.t = t
    
    def calculo_parametro_A(self):
        """
        Calcula el parámetro A de la componente estacional.
        
        Returns:
            float: el parámetro A.
        """
        suma = 0
        for i in range(0,len(self.serie)):
            suma = suma + self.serie[i]*np.sin(self.w*(self.t[i]))
        A = (2/len(self.serie))*suma
        return A
    
    def calculo_parametro_B(self):
        """
        Calcula el parámetro B de la componente estacional.
        
        Returns:
            float: el parámetro B.
        """
        suma = 0
        for i in range(0,len(self.serie)):
            suma = suma + self.serie[i]*np.cos(self.w*(self.t[i]))
        B = (2/len(self.serie))*suma
        return B
    
    def calculo_parametro_R(self):
        """
        Calcula el parámetro R de la componente estacional.
        
        Returns:
            float: el parámetro R.
        """
        A = self.calculo_parametro_A()
        B = self.calculo_parametro_B()
        R = (A**2+B**2)**(1/2)
        return R