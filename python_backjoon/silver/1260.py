from collections import deque

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''


# DFS와 BFS로 출력

# def dfs(graph, v, n):
#     global visited
#     stack = [v]
#     visited[v] = True
#     print(v, end=' ')
#     while stack:
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 stack.append(i)
#                 dfs(graph, i, n)
#             elif not stack:
#                 break
#             else:
#                 stack.pop()

def dfs(v):
    visited[v] = True  # 방문 기록
    print(v, end=' ')
    for i in graph[v]:  # dfs 탐색 재귀 함수
        if not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])  # deque
    visited[v] = True
    while queue:  # stack이 빌 때까지
        v = queue.popleft()  # 선입선출 FiFo
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)



# N : 정점의 개수
# M : 간선의 개수
# V : 시작할 정점 번호
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)
for i in graph:
    i.sort()

# print(graph)

visited = [False] * (N + 1)
dfs(V)
print()

visited = [False] * (N + 1)
bfs(V)
