product = {'name': 'Pen', 'price': 14.99,
           'imported': True, 'stock': 793}

for key in product:
    print(key)

print('___________')

for value in product.values():
    print(value)


print('___________')


for key, value in product.items():
    print(key, '=', value)

print(key, value)