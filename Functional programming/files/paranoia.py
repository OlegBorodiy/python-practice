import os

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z')

move = 1

with open('text.txt', 'w') as infile:
    for _ in range(4):
        infile.write('Hello' + '\n')

outfile = open('cipher_text.txt', 'w')

with open('text.txt', 'r') as infile:
    for string in infile:
        new_line = str()
        for sym in list(string[:-1]):
            if sym == sym.upper():
                new_index = alphabet.index(sym.lower()) + move
                new_line += str(alphabet[new_index]).upper()
            else:
                new_index = alphabet.index(sym) + move
                new_line += str(alphabet[new_index])
        move += 1
        outfile.write(new_line + '\n')

outfile.close()



