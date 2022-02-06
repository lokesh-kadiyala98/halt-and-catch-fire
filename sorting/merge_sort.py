def merge(left, right):
    left_index = right_index = 0
    arr = [0] * (len(left) + len(right))
    index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            arr[index] = left[left_index]
            left_index += 1
        else:
            arr[index] = right[right_index]
            right_index += 1
        index += 1

    while left_index < len(left):
        arr[index] = left[left_index]
        index += 1
        left_index += 1

    while right_index < len(left):
        arr[index] = right[right_index]
        index += 1
        right_index += 1
        
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    return merge(left, right)

arr = merge_sort([175, 8, 9, 3, -2, -13, -150])
print(arr)