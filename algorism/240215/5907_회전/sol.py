import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    num_lst = list(map(int, input().split()))
    for _ in range(M):
        num_lst.append(num_lst.pop(0))
    print(f'#{t} {num_lst[0]}')
