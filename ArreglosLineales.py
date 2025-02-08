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
        
x = Estructura()

x.insertar("hola")
x.insertar("Juan")
x.insertar("Lopez")
x.insertar("Acosta")
x.insertar("Isa")

x.insertarNP(0,"True")
x.insertarNP(1, "Juan")
x.insertarNP(2, "Lopez")
x.insertarNP(3, "Bernardo")
x.insertarNP(4, "Isa")

print(x.arreglo)
print(x.arregloNP)

x.borrar("hola")
print(x.arreglo)

x.borrarNP(0)
x.eliminarultimo()

print(x.arregloNP)
print(x.arreglo)

x.modificarPorI(0, "Bernardo")
x.modificarPorV("Lopez", "Sofi")
print(x.arreglo)

x.modificarPorINP(0, "Bernardo")
x.modificarPorVNP("Lopez", "Sofi")
print(x.arregloNP)