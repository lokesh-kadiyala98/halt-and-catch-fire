# * *
'''
input format:
n - size of the queqe
arr - array of size n

sample input:
4
4 3 1 2

sample output:
3

explaination:
Given array [4, 3, 1, 2]
After swapping (4, 1) we get [1, 3, 4, 2]
After swapping (3, 2) we get [1, 2, 4, 3]
After swapping (4, 3) we get [1, 2, 3, 4]
So, we need a minimum of 3 swaps to sort the array in ascending order.

constraints
1 <= arr[i] <= n
'''

from pathlib import Path

def minimumSwaps(arr):
    index = {}
    swaps = 0

    for i in range(len(arr)):
        index[arr[i]] = i

    for i in range(len(arr) - 1):
        if (arr[i] != i+1):
            swap_index = index[i+1]
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            index[arr[swap_index]] = swap_index
            index[arr[i]] = i
            swaps += 1

    return swaps

if __name__ == '__main__':
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'min_swaps_tc-14.txt'
    f = file_location.open()

    lines = f.readlines()

    # n = int(input())

    arr = list(map(int, lines[1].rstrip().split()))

    res = minimumSwaps(arr)

    print(res)