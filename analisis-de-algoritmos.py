import time
import random

# Bubble sort
# https://www.w3schools.com/python/python_dsa_bubblesort.asp
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion sort
# https://www.w3schools.com/python/python_dsa_insertionsort.asp
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr.pop(i)
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)

# Merge sort
# https://www.w3schools.com/python/python_dsa_mergesort.asp
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)

    return merge(sortedLeft, sortedRight) 

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Función para medir tiempos
# utilizamos time.perf_counter() para medir el tiempo de ejecución porque es más preciso
# repetimos la ejecucion 5 veces y calculamos el promedio
def medir_tiempo_promedio(func, datos, repeticiones=5):
    total = 0
    for _ in range(repeticiones):
        lista_copia = datos.copy()
        inicio = time.perf_counter()
        func(lista_copia)
        fin = time.perf_counter()
        total += (fin - inicio)
    return total / repeticiones

# Creacion de listas aleatorias y llamado a funciones
# se formatea a 4 decimales
tamaño = 100 # Tamaño de la lista a ordenar
datos = [random.randint(1, 10000) for _ in range(tamaño)]

print(f"Tamaño de lista: {tamaño}")

tiempo_promedio_bubble = medir_tiempo_promedio(bubble_sort, datos)
print(f"Bubble Sort: {tiempo_promedio_bubble:.4f} segundos")

tiempo_promedio_insertion = medir_tiempo_promedio(insertion_sort, datos)
print(f"Insertion Sort: {tiempo_promedio_insertion:.4f} segundos")

tiempo_promedio_merge = medir_tiempo_promedio(merge_sort, datos)
print(f"Merge Sort: {tiempo_promedio_merge:.4f} segundos")