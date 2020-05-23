

def cyclic_sort(arr):

    for k, v in enumerate(arr):
        if v != k + 1:
            arr[k], arr[v-1] = arr[v-1], arr[k]
    return arr

print cyclic_sort([2,6,4,3,1,5])
