# 8.2.1 Übung 1

print('8.2.1 Übung 1')
tupel = (15, 13.4, 'Hallo', 2, 'Welt', 156, 2314.341, 'test!', 592312, 123.4567)
print(tupel[1])
tupel2 = tupel[1:-1]
print(tupel2)

# 8.2.2 Übung 2

print('8.2.2 Übung 2')
tupel3 = tupel * 3
print(tupel3)

tupel4 = tupel + tupel + tupel
print(tupel4)

# 8.2.3 Übung 3

print('8.2.3 Übung 3')
tupel5 = tupel3[::-1]
print(tupel5)

# 8.2.4 Übung 4

print('8.2.4 Übung 4')
tupel6 = tupel3[::2]
print(tupel6)

# 8.2.5 Übung 5

print('8.2.5 Übung 5')
print('Hallo' in tupel3)