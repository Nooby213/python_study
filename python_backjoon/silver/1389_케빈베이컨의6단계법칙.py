import sys

input = sys.stdin.readline
from collections import deque


def edge(n, cnt):
    global temp_cnt
    q = deque([(n, cnt)])
    while q:
        num, cnt = q.popleft()
        for k in adj[num]:
            if visited[k] == 0:
                visited[k] = 1
                temp_cnt += cnt
                q.append((k, cnt + 1))


# 유저의 수 N, 2 ≤ N ≤ 100
# 친구 관계의 수 M, 1 ≤ M ≤ 5,000
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
adj = [[] for _ in range(N + 1)]
for i in range(M):
    adj[edges[i][0]].append(edges[i][1])
    adj[edges[i][1]].append(edges[i][0])
# print(adj)
mini_cnt = 5001
mini_friend = 101
for i in range(1, N + 1):
    temp_cnt = 0
    visited = [0] * (N + 1)
    visited[i] = 1
    edge(i, 1)
    if temp_cnt < mini_cnt:
        mini_cnt = temp_cnt
        mini_friend = i
    # print(temp_cnt)
print(mini_friend)
