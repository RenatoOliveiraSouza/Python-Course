def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular



if __name__ == '__main__':
    dobro = multiplicar(2)
    triplo = multiplicar(3)
    print(dobro, triplo)
    print(f' O Triplo de 3 eh {triplo(3)}')
    print(f'O Dobro de 7 eh {dobro(7)}')


 