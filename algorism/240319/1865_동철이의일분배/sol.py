import sys

sys.stdin = open('input.txt')


def can_do(n, temp):
    global maxi

    # 확률은 1보다 작기 때문에 곱할 수록 작아진다
    if temp <= maxi:
        return
    # N번 작업까지 다 했다면, 최대확률 비교
    if n == N:
        maxi = max(maxi, temp)
        return



    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            can_do(n + 1, temp * (can[n][i] * 10 ** -2))
            visited[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    can = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    maxi = 0
    can_do(0, 1)
    print(f'#{t} {format(round(maxi*100, 6),"6f")}')