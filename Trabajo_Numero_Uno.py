import numpy as np

arreglo = []
arregloNP = np.array([True, "hola"])
arregloNP = np.insert(arregloNP, 1, True)
arreglo.append("hola")
arreglo.append(1)

class Estructura:
    def __init__(self):
        self.arreglo = []
        self.arregloNP = np.array([], dtype=object)

    def insertar(self, valor):
        self.arreglo.append(valor)
        return self.arreglo

    def insertarNP(self, i, valor):
        tam = len(self.arregloNP)
        if 0 <= i <= tam:
            self.arregloNP = np.insert(self.arregloNP, i, valor)
        else:
            print("Indice no valido")
        return self.arregloNP
    
    def borrar(self, valor):
        if valor in self.arreglo:
            self.arreglo.remove(valor)
        return self.arreglo

    def borrarNP(self, i):
        if i < len(self.arregloNP):
            self.arregloNP = np.delete(self.arregloNP, i)
        return self.arregloNP
    
    def eliminarPorVNP(self, valor):
        i = 0
        while i < len(self.arregloNP):
            if valor == self.arregloNP[i]:
               self.arregloNP = np.delete(self.arregloNP, i)
            break
            i+=1
        return self.arregloNP
    
    def eliminarultimo(self):
        if len(self.arregloNP)>0:
            i = len(self.arregloNP)-1
            self.arregloNP = np.deleteNP(self.arregloNP,i)
        else:
            print("Arreglo vacio")
        return self.arregloNP
            
    def eliminarultimo(self):
        self.arreglo.pop()
    
    def modificarPorI(self, i,valor):
        self.arreglo[i] = valor
     
    
    def modificarPorV(self, valor, valorModificado):
        i=0
        while i< len(self.arreglo):
            if valor == self.arreglo[i]:
                self.arreglo[i]=valorModificado
                break
            i+=1
        
    def modificarPorINP(self, i, valor):
        self.arregloNP[i] = valor
        
        
    def modificarPorVNP(self, valor, valorModificado):
        i=0
        while i< len(self.arregloNP):
            if valor == self.arregloNP[i]:
                self.arregloNP[i]=valorModificado
                break
            i+=1
        
        
    def busqueda(self, valor):
        i=0
        while i< len(self.arregloNP):
            if valor == self.arregloNP[i]:
                print("Si se encuentra el valor", valor)
                break
            i+=1
        
        
    def ordenMayMen(self):
        self.arreglo.sort()
        self.arreglo.reverse()
        
    def ordenMenMay(self):
        self.arreglo.sort()
        
        
    def ordenMayMenNP(self):
        self.arregloNP = np.sort(self.arregloNP)[::-1]

        
    def ordenMenMayNP(self):
        self.arregloNP.sort()
        
x = Estructura()

x.insertar(2)
x.insertar(3)
x.insertar(8)
x.insertar(5)
x.insertar(6)

x.insertarNP(0, 2)
x.insertarNP(1, 3)
x.insertarNP(2, 8)
x.insertarNP(3, 5)
x.insertarNP(4, 6)

print(x.arreglo)
print(x.arregloNP)

x.borrar(2)
print(x.arreglo)

x.borrarNP(0)
x.eliminarultimo()

print(x.arregloNP)
print(x.arreglo)

x.modificarPorI(0, 5)
x.modificarPorV(3, 6)
print(x.arreglo)

x.modificarPorINP(0, 3)
x.modificarPorVNP(3, 10)
print(x.arregloNP)


x.busqueda(5)

x.ordenMayMen()
print(x.arreglo)
x.ordenMenMay()
print(x.arreglo)

x.ordenMayMenNP()
print(x.arregloNP)
x.ordenMenMayNP()
print(x.arregloNP)
#Crear una función de ordenamiento ascendente y descendente utilizando el archivo presentado en clase. 
#Realicen las acciones necesarias para poder imitar el comportamiento de la función sort() y reverse() en cada caso.
#Estas funciones se deben aplicar para arreglos:
#Tipo list
#Tipo np.array


#funcion ordenamiento acendente
def ordenarMenMay(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#funcion ordenamiento desendente
def ordenarMayMen(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#Ejemplos
mi_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", mi_lista)

# Orden ascendente
listaordenada = ordenarMenMay(mi_lista.copy())
print(listaordenada)

# Orden descendente
listaordenadaINV= ordenarMayMen(mi_lista.copy())
print(listaordenadaINV)


#funcion ordenamiento acendente numpy
def ordenarMenMayNP(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#funcion ordenamiento descendete numpy
def ordenarMayMenNP(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#Ejemplos
mi_array = np.array([64, 34, 25, 12, 22, 11, 90])
print("Arreglo original:", mi_array)

# Orden ascendente
arrayordenadoNP = ordenarMenMayNP(mi_array.copy())
print(arrayordenadoNP)

# Orden descendente
arrayordenadoNPINV = ordenarMayMenNP(mi_array.copy())
print(arrayordenadoNPINV)