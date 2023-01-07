class Nivel_serie():
    def __init__(self, tiempo, parados):
        self.tiempo = tiempo
        self.parados = parados
    
    def calculo(self):
        valor_tiempo_media = self.tiempo.mean()
        tiempo_media_0 = self.tiempo - valor_tiempo_media

        beta_0= self.parados.mean()

        beta_1_num = 0
        beta_1_dem = 0
        for i in range (len(tiempo_media_0)):
            auxzt = (self.parados[i]-beta_0)*tiempo_media_0[i]
            beta_1_num += beta_1_num + auxzt
            auxt2 = tiempo_media_0[i] * tiempo_media_0[i]
            beta_1_dem  += beta_1_dem  + auxt2

        beta_1 = beta_1_num / beta_1_dem

        tendencia = beta_0 + beta_1*tiempo_media_0
        
        return tendencia
