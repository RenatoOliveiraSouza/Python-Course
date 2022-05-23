class Humano:
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Home Neanderthalensis'
        return self


if __name__ == '__main__':
    jose = Humano('Jose')
    gronk = Humano('Gronk').das_cavernas()  

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jose.especie: {jose.especie}')
    print(f'Gronk.especi: {gronk.especie}')