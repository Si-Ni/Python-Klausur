# 9.6.1 Übung 1

print('9.6.1 Übung 1:')
L = list(range(1, 13))
print(L)
L[0] = 13
print(L)

# 9.6.2 Übung 2

print('9.6.2 Übung 2:')
del L[2:7]
print(L)
L[3:6] = range(14, 22)
print(L)

# 9.6.3 Übung 3

print('9.6.3 Übung 3:')
L.append(22)
L.append(23)
L.append(24)
L.append(25)
L.append(26)
print(L)
L2 = list(range(27, 32))
L.extend(L2)
print(L)

# 9.6.4 Übung 4

print('9.6.4 Übung 4:')
L.pop()
print(L)
L[-1:] = []  # oder L[:] = L[:-1] (wenn nur L statt L[:] dann wird ein neues Objekt erzeugt)
print(L)
del L[-1]
print(L)

# 9.6.5 Übung 5

print('9.6.5 Übung 5:')
L = list(reversed(L))  # oder L.reverse()
print(L)

# 9.6.6 Übung 6

print('9.6.6 Übung 6:')
L3 = list(zip(L[0:5], L[5:10]))
print(L3)

# 9.6.7 Übung 7

print('9.6.7 Übung 7:')
L4 = list()
for x in L:
    L4.append(x * 10)
print(L4)
L5 = [x*10 for x in L]
print(L5)

# 9.6.8 Übung 8

print('9.6.8 Übung 8:')


def sortieren(L, key=False):
    L.sort()
    if(key):
        LGerade = list()
        LUngerade = list()
        for x in L:
            if(x % 2 == 0):
                LGerade.append(x)
            else:
                LUngerade.append(x)
        L = []
        L.extend(LGerade)
        L.extend(LUngerade)
    print(L)


sortieren(L, key=True)


##############################################


def my_sort(value):
    return value % 2


sorted(L, key=my_sort)