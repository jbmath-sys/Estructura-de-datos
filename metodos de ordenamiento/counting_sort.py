def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    resultado = []
    for i, c in enumerate(count):
        resultado.extend([i] * c)
    return resultado

# Ejemplo
lista = [4, 2, 2, 8, 3, 3, 1]
print("Ordenado:", counting_sort(lista))

