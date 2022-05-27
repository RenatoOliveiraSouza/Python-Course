lista_1 = [1,2,3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))


lista_2 = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'Jose', 'idade': 26},
]

so_nome = map(lambda p: p['nome'], lista_2)
print(list(so_nome))

so_idade = map(lambda p: p['idade'], lista_2)
print(list(so_idade))

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista_2)
print(list(frases))


