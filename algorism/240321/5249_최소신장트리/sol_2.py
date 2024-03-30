import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush
def prim(start):
    heap =[]
    visited = [0] * (V + 1)

    sum_weight = 0

    heappush(heap, (0, start))

    while heap:
        weight, now = heappop(heap)

        if visited[now]:
            continue

        visited[now] = 1
        sum_weight += weight

        for next in range(V + 1):
            if graph[now][next] and not visited[next]:
                heappush(heap, (graph[now][next], next))
                
    print(f'#{t} {sum_weight}')

# 1 <= T <= 50
T = int(input())
for t in range(1, T + 1):
    # 1 <= V <= 1000, 1 <= w <= 10, 1 <= E <= 1000000
    V, E = map(int, input().split())
    graph = [([0] * (V + 1)) for _ in range(V + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    prim(0)

