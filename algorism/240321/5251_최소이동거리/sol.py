import sys

sys.stdin = open('input.txt')
from heapq import heappop, heappush


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        weight, now = heappop(q)

        if distance[now] < weight:
            continue

        for w, to in adj[now]:
            new_weight = w + weight

            if new_weight >= distance[to]:
                continue

            distance[to] = new_weight
            heappush(q, (new_weight, to))




T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    inf = float('inf')
    distance = [inf] * (N + 1)
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))

    dijkstra(0)
    print(f'#{t} {distance[N]}')