word = 'paralelepipedo'

for  letter in word:
    print(letter, end=',')
print('END')

approveds = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for name in approveds:
    print(name)

for position, name in enumerate(approveds):
    print(f'{position + 1})', name)

week_days =('Sunday', 'Monday', 'Tuesday', 
             'Wednesday','Thursday', 'Friday', 'Saturday')
for day in week_days:
    print(f'Today is {day}')

for letter in set('very cool'):
    print(letter)

for number in {1, 2, 3, 4, 5, 6}:
    print(number)

