import os
import sys
import shutil
import time

#23.6.1
print('23.6.1 Übung Systemfunktionen:')
print(os.getcwd())

#23.6.2
print('23.6.2 Übung Systemfunktionen:')
print(sys.version)

#23.6.3
print('23.6.3 Übung Systemfunktionen:')
os.chdir('./io')
print(os.getcwd())
print(os.listdir())

#23.6.4
print('23.6.4 Übung Systemfunktionen:')
print(os.path.join('/home', 'user14', 'data'))

#23.6.5
print('23.6.5 Übung Systemfunktionen:')
if os.path.isfile('data.txt'):
    print("Datei")
elif os.path.isdir('data.txt'):
    print("Verzeichnis")

#23.6.6
print('23.6.6 Übung Systemfunktionen:')
shutil.copy('./data.txt', '/home/user14/data')
print('Datei wurde kopiert')

#23.6.7
print('23.6.7 Übung Systemfunktionen:')
os.chdir('/home/user14/data')
currenttime = time.time()
for root, dirs, files in os.walk('/home/user14/data/'):
    for file in files:
        file = os.path.join(root, file)
        access_time = os.path.getatime(file)
        since_access = currenttime - access_time
        if since_access <= 86400:
            print(file)