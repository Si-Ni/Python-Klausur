# 12.1.1 Übung 1

print('12.1.1 Übung 1:')


def einsBisZehnAusgeben():
    for x in range(0, 10):
        print(x)


einsBisZehnAusgeben()

# 12.1.2 Übung 2

print('12.1.2 Übung 2:')


def zahlVerdoppeln(zahl):
    return zahl * 2


print(zahlVerdoppeln(4))

# 12.1.3 Übung 3

print('12.1.3 Übung 3:')


def stringsKonkatenieren(a, b):
    return a + b


print(stringsKonkatenieren(a="abc", b="def"))
print(stringsKonkatenieren(b="def", a="abc"))

# 12.1.4 Übung 4

print('12.1.4 Übung 4:')


def mittelwertBerechnen(z1, z2, z3):
    sum = z1 + z2 + z3
    return sum / 3


print(mittelwertBerechnen(4, 6, 8))

# 12.1.5 Übung 5

print('12.1.5 Übung 5:')


def mittelwertBerechnen2(z1, z2, z3=None):
    if(z3 is None):
        sum = z1 + z2
        return sum / 2
    else:
        sum = z1 + z2 + z3
        return sum / 3


print(mittelwertBerechnen2(4, 6, 8))
print(mittelwertBerechnen2(4, 6))

# 12.1.6 Übung 6

print('12.1.6 Übung 6:')
import time


def zeitMessen(func, *parameters):
    start = time.perf_counter_ns()
    func(*parameters)
    end = time.perf_counter_ns()
    print("Benötigte Zeit: " + str(end - start) + 'ns')


zeitMessen(mittelwertBerechnen2, 2, 4, 5)