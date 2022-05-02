FORBIDDEN_WORD = ('soccer', 'religion', 'policy')
texts = [
    'Joan like soccer and policy', 
    'The beach was fun',
]

for text in texts:
    for word in text.lower().split():
        if word in FORBIDDEN_WORD:
            print('Text has a forbidden word:', word)
            break
    else:
        print('Authorized text:', text)