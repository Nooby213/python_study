import sys
sys.stdin = open('input.txt')
def mini_cost(n, temp_cost):
    global mini
    if temp_cost >= mini:
        return

    if n == N:
        mini = min(mini, temp_cost)
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            mini_cost(n + 1, temp_cost + factories[n][i])
            visited[i] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    factories = [list(map(int, input().split())) for _ in range(N)]
    mini = 100*N
    visited = [0] * N
    mini_cost(0, 0)
    print(f'#{t} {mini}')