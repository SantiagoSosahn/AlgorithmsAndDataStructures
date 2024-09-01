def merge_sort(arreglo): 
    if len(arreglo)<=1:
        return arreglo
    else:
        middle = len(arreglo) // 2
        left_arreglo = arreglo[:middle]
        right_arreglo = arreglo[middle:]
        
    left_sorted = merge_sort(left_arreglo)
    right_sorted = merge_sort(right_arreglo)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    print("lista left")
    print(left)
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
        
    print("left despues de ordenar")
    print(left)
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = merge_sort(arr)
print(sorted_arr)