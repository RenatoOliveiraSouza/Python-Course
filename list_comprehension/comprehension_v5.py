dicionario = {i: i *2 for i in range(10) if i % 2 == 0}
print(dicionario)

for number, double in dicionario.item():
    print(f'{number} x 2 = {double}')