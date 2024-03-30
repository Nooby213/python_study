import sys

sys.stdin = open('input.txt')

def group(n):
    if visited[n]:
        return False
    visited[n] = 1
    for i in adj[n]:
        if visited[i] == 0:
            group(i)
    return True

T = int(input())

for t in range(1, T + 1):
    # 1~N번, M장의 신청서
    # 2 <= N <= 100, 1 <= M <= 100
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    edge = list(map(int, input().split()))
    visited = [0] * (N + 1)
    cnt = 0
    for i in range(M):
        adj[edge[2 * i]].append(edge[2 * i + 1])
        adj[edge[2 * i + 1]].append(edge[2 * i])

    for i in range(1, N + 1):
        if group(i):
            cnt += 1
            
    print(f'#{t} {cnt}')