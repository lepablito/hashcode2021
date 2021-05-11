import math
class Street():
    def __init__(self, sal, lle, name, L, visitas):
        self.sal = sal
        self.lle = lle
        self.name = name
        self.L = L
        self.visitas = visitas

    

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

path = 'D:\\Documentos\\Programas\\Hash Code 2021\\Datos\\a.txt'
datos = leer_fichero(path)
datos = [linea.split() for linea in datos]

params = [int(x) for x in datos[0]]

D = params[0] # duracion 
I = params[1] # intersec
S = params[2] # calles
V = params[3] # coches
F = params[4] # bonus


inters = []
cars = []
streets=[]

for i in range(0, I+1):
    inters.append(Intersec(i, []))

for i in range(1, S+1):
    streets.append(Street(datos[i][0],datos[i][2],datos[i][2],datos[i][3], 0))
    inters[int(datos[i][1])].calles.append(datos[i][2])

for i in range(S, S+V+1):
    for j in range(1,int(datos[i][0])+1):
        index = next((k for k, item in enumerate(streets) if item.name == datos[i][j]), -1)
        streets[index].visitas+=1
    #cars.append(Car(datos[i][0], datos[i][1:] ))

print(streets[0].visitas, streets[0].name)


with open('D:\\Documentos\\Programas\\Hash Code 2021\\a.out', 'w') as output:
    output.write(str(I) + '\n')
    for i in range(I):
        output.write(str(i) + '\n')
        output.write(str(len(inters[i].calles)) + '\n')

        for j in range(len(inters[i].calles)):
            index = next((k for k, item in enumerate(streets) if item.name == inters[i].calles[j]), -1)
            if (streets[index].visitas>=1):
                output.write(inters[i].calles[j] + ' 1\n')
            