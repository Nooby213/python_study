import sys

input = sys.stdin.readline

zero_floor = [i for i in range(15)]
apartment = [[0] * 15 for _ in range(15)]
apartment[0] = zero_floor

def how_many(K, N):

    if apartment[K][N]:
        return apartment[K][N]

    for i in range(1, N + 1):
        apartment[K][N] += how_many(K - 1, i)

    return apartment[K][N]

T = int(input())
for _ in range(T):
    # a[b] == a-1[1:b+1]
    # 1 ≤ k, n ≤ 14
    k = int(input())
    n = int(input())

    print(how_many(k, n))
