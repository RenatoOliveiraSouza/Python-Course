def get_day_type(day):
    days = {
        1: 'weekend',
        2: 'week day',
        3: 'week day',
        4: 'week day',
        5: 'week day',
        6: 'week day',
        7: 'weekend',
    }
    return days.get(day, '**INVALID**')


if __name__ == '__main__':
    for day in range(8):
        print(f'{day}: {get_day_type(day)}')
