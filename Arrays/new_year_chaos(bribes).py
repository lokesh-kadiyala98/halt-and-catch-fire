# * *
'''
input format:
t - number of test cases

each test case contains
n - size of the queqe
arr - order of people in the queue

sample input:
2
5
2 1 5 3 4
5
2 5 1 3 4

sample output:
3
Too chaotic

explaination:
test case 1:
person 2 has bribed person 1
person 5 has bribed person 4, 3
so, total bribes = 3

test case 2:
person 4 has bribed more that 2 people(4, 3, 1)
hence, 'Too chaotic'
'''

def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q)):
        if q[i] - i - 1 > 2:
            return 'Too chaotic'
        for j in range(q[i] - 2, i):
            if q[j] > q[i]:
                bribes += 1
    return bribes - 1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))