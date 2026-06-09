import datetime

class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    def __str__(self):
        return f"Festival Musical: {self.nombre}, País: {self.pais}, Estilo Musical: {self.estilo_musical}"
    
    def festival_metodo(self):
        print(f"El mejor festival es: {self.nombre}")

    @classmethod
    def valor_ticket(cls, valor):
        cls.valor_ticket = valor
        return print("El valor del ticket es: ", cls.valor_ticket)
    
    @staticmethod
    def dia_evento(dia):
        if(dia.weekday() == 5 or dia.weekday() == 6):
            return print("El evento es en fin de semana")
        else:
            return print("El evento es un día laborable")

festival1 = FestivalMusical("Lollapalooza", "Estados Unidos", "Rock")
#festival2 = FestivalMusical("Tomorrowland", "Bélgica", "Música electrónica")

FestivalMusical.valor_ticket(150)   

dia1= datetime.date.today()

print(festival1)
print(festival1.nombre)
#print(festival2.nombre)  

print(FestivalMusical.valor_ticket)
print(festival1.valor_ticket)

#print(FestivalMusical.festival1)
#print(festival1.__dict__)
#print(FestivalMusical.__dict__ )
