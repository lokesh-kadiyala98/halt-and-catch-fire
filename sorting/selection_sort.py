def selection_sort(arr):
    for i in range(0, len(arr)-1):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr

sorted_arr = selection_sort([175, 8, 9, 3, -2, -13, -150])
print(sorted_arr)