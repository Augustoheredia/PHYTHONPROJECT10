class DiaClima:
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    def get_humedad(self):
        return self.__humedad

    def set_humedad(self, humedad):
        self.__humedad = humedad

    def get_presion(self):
        return self.__presion

    def set_presion(self, presion):
        self.__presion = presion

    def __str__(self):
        return f"Temperatura: {self.__temperatura}°C, Humedad: {self.__humedad}%, Presión: {self.__presion} hPa"

class SemanaClima:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia):
        self.dias.append(dia)

    def calcular_promedio_temperatura(self):
        temperaturas = [dia.get_temperatura() for dia in self.dias]
        promedio = sum(temperaturas) / len(temperaturas)
        return promedio

# Ejemplo de uso
semana = SemanaClima()

# Crear objetos DiaClima y agregarlos a la semana
dia1 = DiaClima(25, 60, 1013)
dia2 = DiaClima(28, 70, 1010)
dia3 = DiaClima(22, 55, 1015)
semana.agregar_dia(dia1)
semana.agregar_dia(dia2)
semana.agregar_dia(dia3)

# Calcular y mostrar el promedio semanal de temperatura
promedio_semanal = semana.calcular_promedio_temperatura()
print(f"El promedio semanal de temperatura es: {promedio_semanal:.2f}°C")