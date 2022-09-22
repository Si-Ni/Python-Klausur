# 5.1.2 Übung 2

eingabe = input('Bitte eine Zahl eingeben: ')
zahl = float(eingabe)
untereGrenze = 50
obereGrenze = 100

if untereGrenze <= zahl and zahl <= obereGrenze:
    print('Die eingegebene Zahl liegt innerhalb des Bereiches')
else:
    print('Die eingegebene Zahl liegt ausßerhalb des Bereiches')

if untereGrenze <= zahl <= obereGrenze:
    print('Die eingegebene Zahl liegt innerhalb des Bereiches')
else:
    print('Die eingegebene Zahl liegt ausßerhalb des Bereiches')
