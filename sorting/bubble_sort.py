def bubble_sort(arr):
    for i in range(0, len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        # cute lil' optimization technique
        if not swapped:
            break

    return arr

sorted_arr = bubble_sort([175, 8, 9, 3, -2, -13, -150])
print(sorted_arr)

# optimal scenario
sorted_arr = bubble_sort([1, 111, 77, 83, 151, 189, 191])
print(sorted_arr)