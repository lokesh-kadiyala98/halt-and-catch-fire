# * * *
'''
input format:
N M
N - size of array
M - number of manipulations

Manipulations input format
a b k
a - from
b - to
k - cummulate value

cumulate elems index from(a) to (b) with k

sample input:
5 3
1 2 100
2 5 100
3 4 100

sample output:
200

explaination:
initially arr is [0, 0, 0, 0, 0]
after 3 manipulations [100, 200, 200, 200, 100]
largest of them is 200
'''

def arrayManipulation(n, queries):
    arr = [0] * n
    temp = 0
    largest = 0
    for query in queries:
        [a, b, k] = query
        arr[a-1] += k
        if b<n:
            arr[b] -= k

    for elem in arr:
        temp += elem
        if temp>largest:
            largest = temp

    return largest

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)