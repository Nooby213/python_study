from heapq import heappop, heappush
import sys
sys.stdin = open('input_d.txt')

def dijkstra(s):
    pq = []

    heappush(pq, (0, start))
    distance[s] = 0

    while pq:
        # 최
        now, dist = heappop(pq)

        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_node = to[0]
            next_dist = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 패스
            if new_dist >= distance[next_node]:
                continue

            # 누적 거리를 최단 거리로 갱신
            distance[next_node] = new_dist
            heappush(pq, (next_node, new_dist))

INF = 1e9
V, E = map(int, input().split())
start = 0

# 인접 리스트
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

dijkstra(0)
print(distance)