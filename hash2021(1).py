import math
class Street():
    def __init__(self, sal, lle, name, L):
        self.sal = sal
        self.lle = lle
        self.name = name
        self.L = L

    

class Intersec():
    def __init__(self, id, calles):
        self.id = id
        self.calles = calles

class Car():
    def __init__(self, P, names):
        self.P = P
        self.names = names


def leer_fichero(path):
    with open(path, 'r') as f:
        l = f.readlines()
    l = [x.strip() for x in l]
    return l

path = 'C:\\Users\\pablm\Documents\\HashCode2021\\e.txt'
datos = leer_fichero(path)
datos = [linea.split() for linea in datos]

params = [int(x) for x in datos[0]]

D = params[0] # duracion 
I = params[1] # intersec
S = params[2] # calles
V = params[3] # coches
F = params[4] # bonus


inters = []
streets=[]
longi=[]
for i in range(0, I+1):
    inters.append(Intersec(i, []))

for i in range(1, S+1):
    streets.append(Street(datos[i][0],datos[i][2],datos[i][2],datos[i][3]))
    inters[int(datos[i][1])].calles.append(datos[i][2])

print(streets[0].name)

with open('C:\\Users\\pablm\Documents\\HashCode2021\\e.out', 'w') as output:
    output.write(str(I) + '\n')
    for i in range(I):
        output.write(str(i) + '\n')
        output.write(str(len(inters[i].calles)) + '\n')

        for j in range(len(inters[i].calles)):
            n = len(inters[i].calles)
            index = next((k for k, item in enumerate(streets) if item.name == inters[i].calles[j]), -1)
            dur=math.ceil(int(streets[index].L)/n)
            output.write(inters[i].calles[j] + ' ' + str(dur) +'\n')