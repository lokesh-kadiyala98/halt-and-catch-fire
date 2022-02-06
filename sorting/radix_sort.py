import math

def get_digit_at_place(num, place):
    return math.floor(num / math.pow(10, place)) % 10

def get_num_of_digits(num):
    # handle math domain error
    if num == 0:
        return 1
    return math.floor(math.log10(num)) + 1

def get_most_digits(arr):
    max_digits = 0

    for item in arr:
        max_digits = max(max_digits, get_num_of_digits(item))
    
    return max_digits

def radix_sort(arr):
    sorted_arr = []
    most_digits = get_most_digits(arr)

    for i in range(0, most_digits):
        bucket = [[]] * 10
        for elem in arr:
            hash = get_digit_at_place(elem, i)
            bucket[hash].append(elem)

        for bucket_arr in bucket:
            for elem in bucket_arr:
                sorted_arr.append(elem)
    
    return sorted_arr

print(get_digit_at_place(15486, 4))
print(get_num_of_digits(1))
print(radix_sort([18, 9]))