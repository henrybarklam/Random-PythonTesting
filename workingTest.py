

possible_letters = 'QWRYPDFHJKZXVBNM'
possible_letters = list(possible_letters)
print("works")
l = []
for i in possible_letters:
    for j in possible_letters:
        for x in possible_letters:
            for y in possible_letters:
                for z in possible_letters:
                    if (j == 'M' or x == 'M') and (i == 'P' or j == 'P' or x == 'P' or y == 'P' or z == 'P') and (i == 'H' or j == 'H' or x == 'H' or y == 'H' or z == 'H') and (i == 'Y' or j == 'Y' or x == 'Y' or y == 'Y' or z == 'Y'):
                        print(i+j+x+y+z)

for word in l:
    print(l)