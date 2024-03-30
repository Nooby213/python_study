import sys

sys.stdin = open('input.txt')


# V 개 이내의 노드
# E 개의 간선
# 경로가 있으면 1 없으면 0
def dfs(v):
    stack.append(v)
    if visited[v] == 0:
        visited[v] = 1
        for i in adj[v]:
            if visited[i] == 0:
                dfs(i)




T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())

    visited = [0] * (V + 1)
    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        # adj[b].append(a)
    S, G = map(int, input().split())
    stack = []
    dfs(S)
    # print(stack)
    # print(adj)
    if G in stack:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
