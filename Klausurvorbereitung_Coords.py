import math


def readFile(fileName):
    """Read coordinates out of a file - returns xs, ys as Lists
    """
    xs = []
    ys = []

    with open(fileName) as fobj:
        next(fobj)
        for line in fobj:
            if line.strip():
                x, y = line.split(", ")
                xs.append(float(x))
                ys.append(float(y))
    return(xs, ys)


xs, ys = readFile('coords.txt')
print(xs, ys)


def readFileAsDic(fileName):
    """Read coordinates out of a file - returns xs, ys as Lists of a dictionary
    """
    output = {}
    xs = []
    ys = []

    with open(fileName) as fobj:
        par1, par2 = fobj.readline().strip().split(", ")
        for line in fobj:
            if line.strip():
                x, y = line.split(", ")
                xs.append(float(x))
                ys.append(float(y))
        output[par1] = xs
        output[par2] = ys
    return(output)


dicData = readFileAsDic('coords.txt')
print(dicData)


def sum_lists(xs, ys):
    """sums the values in two given lists"""
    return(sum(xs), sum(ys))


def sum_dict(data):
    """sums the values of the lists in a dictionary"""
    keys = data.keys()
    output = ()
    for key in keys:
        output = output + (sum(data[key]),)
    return output


print(sum_lists(xs, ys))
print(sum_dict(dicData))
print(sum_lists(xs, ys) == sum_dict(dicData))


class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = math.sqrt((x*x)+(y*y))

    def __repr__(self):
        return "Coord({}, {})".format(self.x, self.y)

    def __add__(coord1, coord2):
        return Coord(coord1.x + coord2.x, coord1.y + coord2.y)


coord1 = Coord(2, 3)
print(coord1.dist)

print(coord1)

coords = []
for x, y in zip(xs, ys):
    coords.append(Coord(x, y))
print(coords[0].x, coords[0].y)

coord2 = Coord(7, 2)
addedCoord = coord1 + coord2
print(addedCoord)