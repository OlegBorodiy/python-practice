goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for keys in goods:
    sum_rub = 0
    amount = 0
    for coup in store[goods[keys]]:
        sum_rub += coup['quantity'] * coup['price']
        amount += coup['quantity']
    print(keys, '-', amount, 'шт, стоимость', sum_rub, 'руб')


# Лампа - 27 шт, стоимость 1134 руб
# Стол - 54 шт, стоимость 27860 руб
# Диван - 3 шт, стоимость 3550 руб
# Стул - 105 шт, стоимость 10311 руб
