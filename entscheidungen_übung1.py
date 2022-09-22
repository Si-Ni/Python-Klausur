# 5.1.1 Übung 1

eingabe = input('Bitte eine Zahl eingeben: ')
zahl = float(eingabe)
grenzwert = 100

if zahl < grenzwert:
    print('Die eingegebene Zahl ist kleiner als der Grenzwert', grenzwert)
elif zahl > grenzwert:
    print('Die eingegebene Zahl ist größer als der Grenzwert ' + str(grenzwert))
else:
    print('Die eingegebene Zahl ist gleich dem Grenzwert ' + str(grenzwert))