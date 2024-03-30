import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
for i in range(N - 1):
    num_lst[i + 1] += num_lst[i]
for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(num_lst[j - 1])
    else:
        print(num_lst[j - 1] - num_lst[i - 2])
