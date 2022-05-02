FORBIDDEN_WORDS = {'soccer', 'religion', 'policy'}
texts = [
    'Joan like soccer and policy', 
    'The beach was fun',
]

for text in texts:
    intersection = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersection:
        print('Text has forbidden words:', intersection)
    else:
        print('Authorized text:', text)

