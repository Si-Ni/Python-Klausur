# 22.5.* Übung Strings

print('22.5.1 Übung Strings:')
import os
output = "Das soll in der Mitte stehen"
centeredOutput = output.center(os.get_terminal_size()[0], '!')
print(centeredOutput)

print('22.5.2 Übung Strings:')
onlyNumbersString = "124567"
onlyLettersString = "abcDEF"
mixedString = "df352xX"

print(onlyNumbersString + " besteht nur aus Zahlen: ", onlyNumbersString.isdecimal())
print(onlyNumbersString + " besteht nur aus Buchstaben: ", onlyNumbersString.isalpha())
print(onlyLettersString + " besteht nur aus Zahlen: ", onlyLettersString.isdecimal())
print(onlyLettersString + " besteht nur aus Buchstaben: ", onlyLettersString.isalpha())
print(mixedString + " besteht nur aus Zahlen: ", mixedString.isdecimal())
print(mixedString + " besteht nur aus Buchstaben: ", mixedString.isalpha())
print(mixedString + " besteht nur aus Buchstaben oder Zahlen: ", mixedString.isalnum())

print('22.5.3 Übung Strings:')

givenString = "Dieser Satz soll durch Unterstriche verbunden werden"
print(givenString)
stringList = givenString.split(" ")
print(stringList)
joinedString = "_".join(stringList)
print(joinedString)

print('22.5.4 Übung Strings:')
template = """
Hallo {name},
du schuldest mir noch {schuldbetrag:.2f}€.
Bitte denk daran mir den Betrag von {schuldbetrag:.2f}€ bis morgen zu überweisen.
Ich brauche das Geld ({schuldbetrag:.2f}€) sehr dringend.
MfG
"""
name = "Paul"
schuldbetrag = 235.50

print(template.format(**{"name": name, "schuldbetrag": schuldbetrag}))