# * *
'''

You are given an array and you need to find number of tripets of indices (i, j, k) such that 
the elements at those indices are in geometric progression for a given common ratio r and i < j < k.

input format:
n r
arr

n - size of the queqe
r - common ratio
arr - order of people in the queue

sample input:
6 3
1 3 9 9 27 81

sample output:
6

explaination:
triplets satisfying are (0, 1, 2), (0, 1 3), 
(1, 2, 4), (1, 3, 4), (2, 4, 5), (3, 4, 5)

test case 2:
person 4 has bribed more that 2 people(4, 3, 1)
hence, 'Too chaotic'
'''

from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    res = 0
    rc = defaultdict(int)
    lc = defaultdict(int)

    for elem in arr:
        rc[elem] += 1

    for mp in arr:
        lp = mp // r
        rp = mp * r
        rc[mp] -= 1
        if lc[lp] and rc[rp] and mp%r==0:
            res += lc[lp] * rc[rp]
        lc[mp] += 1

    return res

if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)