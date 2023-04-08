am_friends = int(input('Кол-во друзей: '))
credits_pap = int(input('Долговых расписок: '))
list_friends = []

for fri in range(am_friends):
    list_friends.append(0)

for num_pap in range(credits_pap):
    print()
    print(num_pap + 1, 'расписка')
    out = int(input('Кому: '))
    from_fr = int(input('От кого: '))
    amount = int(input('Сколько: '))
    list_friends[out - 1] -= amount
    list_friends[from_fr - 1] += amount

print('\nБаланс друзей: ')

for index in range(am_friends):
    print(index + 1, ':', list_friends[index])