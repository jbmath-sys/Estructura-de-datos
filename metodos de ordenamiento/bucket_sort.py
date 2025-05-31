def bucket_sort(arr):
    if not arr:
        return []
    buckets = [[] for _ in range(10)]
    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)
    return resultado

# Ejemplo
lista = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Ordenado:", bucket_sort(lista))
