def age_group(age):
    if 0 <= age < 18:
        return 'Minor'
    elif age in range(18, 64):
        return 'Adult'
    elif age in range(65, 100):
        return 'Best Age'
    elif age >= 100:
        return 'Centenary'
    else:
        return 'Invalid age'


if __name__ == '__main__':
    for age in (17, 35, 87, 113, -2):
        print(f'{age}: {age_group(age)}')
