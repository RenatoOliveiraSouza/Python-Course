def get_type_day(day):
    days = {
        (1, 7): 'Weekend',
        tuple(range(2,7)): 'week day',
    }
    choosen_day = (type for numbers, type in days.items() if day in numbers)
    return next(choosen_day, '** INVALID DAY **')


if __name__ == '__main__':
    for day in range(0, 9):
        print(f'{day}: {get_type_day(day)}')
