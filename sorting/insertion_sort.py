def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr

sorted_arr = insertion_sort([175, 8, 9, 3, -2, -13, -150])
print(sorted_arr)