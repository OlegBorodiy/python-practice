string = input('Сообщение: ')
new_string = string.split(' ')

for word in new_string:
    if word.isalpha():
        print(word[::-1], end=' ')
    else:
        count = len(word) - 1
        while True:
            for sym in word[::-1]:
                if sym.isalpha():
                    count -= 1
                else:
                    break
            break
        print(word[count - 1::-1] + word[count] +
              word[:count:-1], end=' ')
