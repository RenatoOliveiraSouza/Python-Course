def cores_arco_iris(): 
    yield 'Vermelho'
    yield 'Laranja'
    yield 'Amarelo'
    yield 'Verde'
    yield 'Azul'
    yield 'Indigo'
    yield 'Violeta'

if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))
        