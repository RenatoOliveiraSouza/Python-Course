from functools import reduce



pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

menores = filter(lambda p: p['idade']< 18, pessoas)
soma_idade_2 = reduce(lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idade_2)

so_idade = map(lambda p: p['idade'], pessoas)
print(list(so_idade))