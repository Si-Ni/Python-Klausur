class Person:

    def __init__(self, name, standort):
        self.name = name
        self.standort = standort


# 15.1.1 Übung Ausnahmen
TestPerson = Person("TestName", "TestStadt")
# print(TestPerson.hobby)

# 15.1.2 Übung Ausnahmen
try:
    print(TestPerson.hobby)
except AttributeError:
    print("Attribut exisitiert nicht")
finally:
    print("fertig")

# 15.1.4 Übung Ausnahmen
L = list(range(1, 6))
try:
    print(L[8])
except IndexError:
    print("Die Liste hat nicht so viele Einträge")

# 15.1.5 Übung Ausnahmen


def my_get(dic, key, default=None):
    try:
        return dic[key]
    except KeyError:
        return default


dic = {'a': 100, 'b': 200}
print(my_get(dic, "c", 300))

# 15.1.6 Übung Ausnahmen


class PositiveOnly(Exception):
    pass


value = -3
if(value < 0):
    raise PositiveOnly(f'Negative Werte nicht erlaubt, gegebener Wert: {value}')