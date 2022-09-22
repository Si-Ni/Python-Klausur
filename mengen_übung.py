# 11.1.1 Übung 1

print('11.1.1 Übung 1:')
s1 = {"Nils", "Luca", "Richard", "Paul", "Robert", "Marius"}
s2 = set(["Luca", "Tom", "Magnus", "Than", "Marius"])

print("Luca" in s2)
print("Tom" in s1)

print("Schnittmenge: ", "")
print(s1.intersection(s2))
print("Differenz s1 - s2: ", "")
print(s1 - s2)
print("Differenz s2 - s1: ", "")
print(s2 - s1)
print("Vereinigung: ", "")
print(s1.union(s2))

# 11.1.2 Übung 2

print('11.1.2 Übung 2:')
sUnter = {"Nils", "Richard", "Paul"}
print(sUnter.issubset(s1))

# 11.1.3 Übung 3

print('11.1.3 Übung 3:')
s3 = {frozenset(["Nils", "Luca"]), frozenset(["Richard", "Paul"]), frozenset(["Robert"])}
s4 = {frozenset(["Richard", "Paul"]), frozenset(["Robert"])}
print(s3.intersection(s4))

# 11.1.4 Übung 4

print('11.1.4 Übung 4:')

menge = set()
for i in range(0, 100000):
    menge.add(i)

import time

searchNumber = 99999

start = time.perf_counter_ns()
searchNumber in menge
end = time.perf_counter_ns()
print('Menge: ' + str(end - start) + 'ns')