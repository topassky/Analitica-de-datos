class Coeficientes_Estacionales():
    def __init__ (self, serie, tiempo):
        self.serie = serie
        self.tiempo = tiempo
    
    def calculo(self):
        media = self.serie.mean()
        print(media)
        coeficiente_estacional = (self.serie - media) / media
        print(coeficiente_estacional)
        return coeficiente_estacional

