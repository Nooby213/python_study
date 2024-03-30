import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(n):
    visited[n] = 1
    for i in adj[n]:
        if visited[i] == 0:
            dfs(i)


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, input().split())
    adj[p].append(c)
    adj[c].append(p)
visited = [0] * (N + 1)
cnt = 0

for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
