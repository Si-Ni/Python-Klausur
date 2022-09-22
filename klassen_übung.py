# 14.2.* Übung Klassen

print('14.2.1 Übung Klassen:')


class Person:

    def __init__(self, name, standort):
        self.name = name
        self.standort = standort

    def gehezu(self, standort):
        self.standort = standort
        print("Die Person: " + self. name + " ist hier hin gegangen: " + self.standort)

    def __rshift__(self, standort):
        self.gehezu(standort)


person1 = Person("Nils", "Zuhause")
person2 = Person("Richard", "Zuhause")
person3 = Person("Maik", "Zuhause")

person1.gehezu("Club")
person2.gehezu("Fußballplatz")
person3.gehezu("Gym")

# 14.3.* Übung Klassen

print('14.3.1 Übung Klassen:')

verboteneOrte = ["Club", "Festival"]


class EingeschraenktePerson(Person):
    def gehezu(self, standort):
        if(standort in verboteneOrte):
            print("Der Zugang zu Ort: " + standort + " ist verboten")
        else:
            super().gehezu(standort)


personEingeschraenkt = EingeschraenktePerson("Ben", "Zuhause")
personEingeschraenkt.gehezu("Club")
personEingeschraenkt.gehezu("Schachclub")

# 14.4.2 Übung Klassen

print('14.4.2 Übung Klassen:')

person4 = Person("Jordan", "Zuhause")
person4 >> 'Schreibtisch'