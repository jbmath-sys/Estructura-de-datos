def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Ejemplo
lista = [10, 7, 8, 9, 1, 5]
print("Ordenado:", quick_sort(lista))
