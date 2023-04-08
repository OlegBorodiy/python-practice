def tup(tuples, element):
    new_tuple = {}
    if element not in tuples:
        return new_tuple
    elif element in tuples and element not in tuples[tuples.index(element) + 1: len(tuples) - 1]:
        new_tuple = tuples[tuples.index(element):]
        return new_tuple
    else:
        new_tuple = tuples[tuples.index(element):tuples.index(element, tuples.index(element) + 1, len(tuples)) + 1]
        return new_tuple


elem = input('Введите любой элемент: ')
old_tuples = ('1', '2', 'Bounty', 9, 'Home', '2', 3, 'Job', 11, '1', 45, 4)

new_tuples = tup(old_tuples, elem)

print(new_tuples)