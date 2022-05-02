FORBIDDEN_WORD = ('soccer', 'religion', 'policy')
texts = [
    'Joan like soccer and policy', 
    'The beach was fun',
]

for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORD:
            print('Text has a forbidden word:', word)
            found = True
            break

if not found:
    print('Authorized text:', text)