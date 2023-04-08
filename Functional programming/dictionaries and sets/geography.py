count = int(input('Кол-во стран: '))
geo = {}
sum_geo = {}

for _ in range(count):
    print(_ + 1, 'страна:', end=' ')
    string = input().split()
    for i in range(len(string) - 1):
        geo[string[i + 1]] = string[0]
        sum_geo.update(geo)

for _ in range(3):
    print()
    print(_ + 1, 'город:', end=' ')
    city = input()
    if city in sum_geo.keys():
        print('Город', city, 'расположен в стране', str(sum_geo[city]) + '.')
    else:
        print('По городу', city, 'данных нет.')