# 16.8.* Übung Eingabe/Ausgabe

print('16.8.1 Übung:')
eingabe = input("Gib deinen Namen ein: ")
print("Hallo " + eingabe)

print('16.8.2 Übung:')
while True:
    eingabe = input("Gib deinen Namen ein: ")
    if eingabe == "end":
        break
    print("Hallo " + eingabe)

print('16.8.3 Übung:')
fobj = open('data_out.txt', 'w')
for i in range(1, 11):
    fobj.write(str(i) + '\n')
print('data_out.txt wurde geändert')

print('16.8.4/5 Übung:')
with open('data_out.txt') as fobj:
    data = fobj.read()
print(data)

with open('data_out.txt') as fobj:
    lines = fobj.read().splitlines()
print(lines)

print('16.8.6 Übung:')
import pickle

data = [1, 2, 3]
with open('data.store', 'wb') as fobj:
    pickle.dump(data, fobj)
with open('data.store', 'rb') as fobj:
    loaded_data = pickle.load(fobj)
print(loaded_data)

print('16.8.6 Übung:')
import argparse

parser = argparse.ArgumentParser(description="set input and output file")
parser.add_argument("-i", "--input", type=str, help="define input file")
parser.add_argument("-o", "--output", type=str, help="define output file")
args = parser.parse_args()

print("Using input file: " + args.input)
print("Using output file: " + args.output)