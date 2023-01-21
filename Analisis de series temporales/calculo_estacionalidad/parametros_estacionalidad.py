import numpy as np

class Parametros_Estacionalidad():
    def __init__(self, serie, w):
        self.serie = serie
        self.w = w
    
    def calculo_parametro_A(self):
        suma = 0
        for i in range(0,len(self.serie)):
            suma = suma + self.serie[i]*np.sin(self.w*(i+1))
        A = (2/len(self.serie))*suma
        return A
    
    def calculo_parametro_B(self):
        suma = 0
        for i in range(0,len(self.serie)):
            suma = suma + self.serie[i]*np.cos(self.w*(i+1))
        B = (2/len(self.serie))*suma
        return B
    
    def calculo_parametro_R(self):
        A = self.calculo_parametro_A()
        B = self.calculo_parametro_B()
        R = (A**2+B**2)**(1/2)
        return R