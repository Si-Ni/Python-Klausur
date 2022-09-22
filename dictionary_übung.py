# 10.2.1 Übung 1

print('10.2.1 Übung 1:')
dic = {'Nils': '015753028345', 'Luca': '015750812938', 'Richard': '0157526289272'}
print(dic['Nils'])
print(dic['Luca'])
print('Richard' in dic)
print('Tom' in dic)
print(dic.values())
print(dic.keys())

# 10.2.2 Übung 2

print('10.2.2 Übung 2:')
print(dic.get('Tom'))
print(dic.get('Tom'), 0)
dic.setdefault('Tom', '0157593289219')
print(dic)

# 10.2.3 Übung 3

print('10.2.3 Übung 3:')
import random

dic2 = dic.copy()
dicNeu = {}
for x in dic2:
    dicNeu[x + '_alt'] = dic2[x]
    dicNeu[x] = str(random.randint(4915750000000, 4915759999999))
print(dicNeu)

# update Methode nutzen

# 10.2.4 Übung 4

print('10.2.4 Übung 4:')

del dicNeu['Luca_alt']
print(dicNeu.pop('Nils_alt'))
print(dicNeu.popitem())
print(dicNeu)

# 10.2.5 übung 5

print('10.2.5 Übung 5:')
dicSearch1 = {}
listSearch1 = []
menge = set()
for i in range(0, 100000):
    dicSearch1[i] = i
    listSearch1.append(i)
    menge.add(i)

import time

searchNumber = 99999

start = time.perf_counter_ns()
searchNumber in dicSearch1
end = time.perf_counter_ns()
print('Dictionary: ' + str(end - start) + 'ns')

start = time.perf_counter_ns()
searchNumber in listSearch1
end = time.perf_counter_ns()
print('List: ' + str(end - start) + 'ns')

start = time.perf_counter_ns()
searchNumber in menge
end = time.perf_counter_ns()
print('Menge: ' + str(end - start) + 'ns')

#  Besseres Erstellen von Liste und Dict
#  L = list(range(10000))
#  d = dict.fromkeys(L)