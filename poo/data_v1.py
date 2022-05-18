class Data:
    def __str__(self):
        return(f'{self.dia}/{self.mes}/{self.ano}')


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 1996
print(d1)

d2 = Data()
d2.dia = 9
d2.mes = 8
d2.ano = 2012
print(d2)

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        return(f'{self.dia}/{self.mes}/{self.ano}')


d1 = Data(5, 12, 1996)
print(d1)

d2 = Data(9, 8, 2012)
print(d2)