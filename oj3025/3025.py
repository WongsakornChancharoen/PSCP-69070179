'''Seasons'''
month = int(input('Enter month'))
day = int(input('Enter day'))

seasons = ['winter', 'spring', 'summer', 'fall']
if not month % 3:
    if day < 21:
        print(seasons[(month // 3) - 1])
    else:
        if month == 12:
            print(seasons[0])
        else:
            print(seasons[month // 3])
else:
    print(seasons[month // 3])
