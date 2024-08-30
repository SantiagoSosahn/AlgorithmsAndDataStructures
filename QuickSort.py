def QuickSort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        pivote = arreglo[len(arreglo)//2]
        element_izq = [x for x in arreglo if x<pivote]
        element_der= [x for x in arreglo if x>pivote]
        element_med = [x for x in arreglo if x == pivote]

        return QuickSort(element_izq) + element_med + QuickSort(element_der)
    
#Ejemplos
Numbers = [23, 2, 32, 43, 12, 14, 54, 32, 35]
arreglo_ordenado = QuickSort(Numbers)
print(arreglo_ordenado)