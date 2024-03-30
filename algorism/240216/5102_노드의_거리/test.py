from collections import deque

def bfs(s, g):
    visited = [0] * (V + 1)
    stack = deque([s])
    visited[s] = 1
    while stack:
        v = stack.popleft()
        # print(v, end=' ')
        for i in adj[v]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = visited[v] + 1

    return visited[g]


V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
# visited = [0] * (V + 1)  # 방문하기 전 노드 거친 횟수

for e in range(E):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

S, G = map(int, input().split())
result = bfs(S, G)

print(f'{result-1}')