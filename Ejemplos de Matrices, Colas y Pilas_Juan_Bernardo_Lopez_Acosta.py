#Ejemplo: Temperaturas Mensuales por Ciudad
#Supongamos que queremos almacenar las temperaturas promedio (en °C) de 3 ciudades durante 12 meses y luego calcular:
#El promedio anual por ciudad.
#El promedio mensual de todas las ciudades.

# Definimos la matriz: 3 ciudades x 12 meses
temperaturas = [
    [25, 26, 24, 22, 20, 18, 17, 18, 19, 21, 23, 24],  # Ciudad A
    [28, 29, 27, 25, 23, 21, 20, 21, 22, 24, 26, 27],  # Ciudad B
    [20, 21, 19, 17, 15, 13, 12, 13, 14, 16, 18, 19]   # Ciudad C
]

ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]

# 1. Promedio anual por ciudad
print("Promedio anual por ciudad:")
for i in range(len(ciudades)):
    promedio_anual = sum(temperaturas[i]) / len(temperaturas[i])
    print(f"{ciudades[i]}: {promedio_anual:.2f}°C")

# 2. Promedio mensual de todas las ciudades
print("\nPromedio mensual de todas las ciudades:")
for mes in range(12):
    total_mes = 0
    for ciudad in range(3):
        total_mes += temperaturas[ciudad][mes]
    promedio_mes = total_mes / 3
    print(f"Mes {mes + 1}: {promedio_mes:.2f}°C")
    
    
    
    #Ejemplo: Historial de Navegación (Usando Pilas)
# Una pila es una estructura LIFO (Last In, First Out), donde el último elemento en entrar es el primero en salir.

# Creamos una pila para el historial de navegación
historial = []

# Función para visitar una página (agregar a la pila)
def visitar_pagina(pila, pagina):
    pila.append(pagina)
    print(f"Has entrado a: {pagina}")

# Función para retroceder (eliminar de la pila)
def retroceder(pila):
    if len(pila) > 0:
        pagina_actual = pila.pop()
        print(f"Has salido de: {pagina_actual}")
        if len(pila) > 0:
            print(f"Ahora estás en: {pila[-1]}")  # Mostrar la página anterior
        else:
            print("No hay más páginas en el historial.")
    else:
        print("El historial está vacío.")

# Simulación de navegación
visitar_pagina(historial, "google.com")
visitar_pagina(historial, "youtube.com")
visitar_pagina(historial, "github.com")

print("\nHistorial actual:", historial)

# Retroceder en el navegador
retroceder(historial)  # Sale de github.com
retroceder(historial)  # Sale de youtube.com
retroceder(historial)  # Sale de google.com
retroceder(historial)  # Historial vacío

#Ejemplo: Cola de Impresión (Usando una Cola)

from collections import deque  # Usamos deque para una cola eficiente

# Creamos una cola para los documentos a imprimir
cola_impresion = deque()

# Función para agregar un documento a la cola
def agregar_documento(cola, documento):
    cola.append(documento)
    print(f"📄 Documento '{documento}' añadido a la cola de impresión.")

# Función para imprimir el próximo documento
def imprimir_documento(cola):
    if len(cola) > 0:
        documento = cola.popleft()  # Extrae el primer elemento
        print(f"🖨️ Imprimiendo: {documento}")
    else:
        print("❌ No hay documentos en la cola.")

# Simulación de impresión
agregar_documento(cola_impresion, "Informe_final.pdf")
agregar_documento(cola_impresion, "Presentación.pptx")
agregar_documento(cola_impresion, "Factura_123.xlsx")

print("\n--- Estado de la cola ---")
print("Documentos pendientes:", list(cola_impresion), "\n")

# Proceso de impresión
imprimir_documento(cola_impresion)
imprimir_documento(cola_impresion)
imprimir_documento(cola_impresion)
imprimir_documento(cola_impresion)  # Intentar imprimir con cola vacía