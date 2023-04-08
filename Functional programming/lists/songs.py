violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

new_list = []
time_s = 0
amount = int(input('Сколько песен выбрать? '))
for i in range(amount):
    print('Название', i + 1, 'песни:', end=' ')
    song = input()
    for index in violator_songs:
        if index[0] == song:
            time_s += index[1]

print('\nОбщее время звучания песен:', round(time_s, 2), 'минут')


