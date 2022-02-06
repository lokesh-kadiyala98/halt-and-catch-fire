def get_pivot(arr, left, right):
    left_most_elem = arr[left]
    pivot = left

    for ptr in range(left, right):
        if arr[ptr] < left_most_elem:
            pivot += 1
            arr[ptr], arr[pivot] = arr[pivot], arr[ptr]

    arr[pivot], arr[left] = arr[left], arr[pivot]

    return pivot

def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = get_pivot(arr, left, right)

    quick_sort(arr, left, pivot)
    quick_sort(arr, pivot+1, right)

    return arr

arr = [175, 8, 9, 3, -2, -13, -150]
sorted_arr = quick_sort(arr, 0, len(arr))
print(sorted_arr)