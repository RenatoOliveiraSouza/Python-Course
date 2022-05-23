class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
                ('Bater em bandidos', 'Atirar teias entre predios')


if __name__ == '__main__':
    john = Homem()
    aranha = Aranha()
    peter = HomemAranha()
    print(f'John: {john.capacidades}')
    print(f'Aranha: {aranha.capacidades}')
    print(f'Peter: {peter.capacidades}')
            


