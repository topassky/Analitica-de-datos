class FrecuenciasYPeriodosBasicos:
    def __init__(self, longitud):
        self.longitud = longitud
        self.frecuencias = []
        self.periodos = []

    def calcular_frecuencias(self):
        for j in range(1, self.longitud // 2 + 1):
            frecuencia = j / self.longitud
            self.frecuencias.append(frecuencia)
        return self.frecuencias

    def calcular_periodos(self):
        for j in range(1, self.longitud // 2 + 1):
            periodo = self.longitud / j
            self.periodos.append(periodo)
        return self.periodos

