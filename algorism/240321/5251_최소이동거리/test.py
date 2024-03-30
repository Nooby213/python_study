import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush


def prim(start):
    heap = []
    visited = [False] * (V + 1)

    sum_weight = 0
    # 초기값
    heappush(heap, (0, start))

    while heap:
        weight, now = heappop(heap)
        # 갔던 곳이면 안감
        if visited[now]:
            continue
        # 방문표시
        visited[now] = True
        # 가중치 합산
        sum_weight += weight
        if now == 2:
            print(sum_weight)
        # 다음 방문지 설정
        for nxt, w in graph[now]:
            if not visited[nxt]:
                heappush(heap, (w, nxt))

    print(f'#{t} {sum_weight}')


# 1 <= T <= 50
T = int(input())
for t in range(1, T + 1):
    # 1 <= V <= 1000, 1 <= w <= 10, 1 <= E <= 1000000
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    # 인접 리스트로 반환
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
        graph[e].append((s, w))

    prim(0)
