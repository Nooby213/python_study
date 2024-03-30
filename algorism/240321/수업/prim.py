'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import sys
sys.stdin = open('input.txt')
# 우선 순위 큐 활용
from heapq import heappush, heappop
def prim(start):
    pq = []
    MST = [0] * V

    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)
        # 방문 했다면 contiunu
        if MST[now]:
            continue
        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight
        # 갈 수 있는 노드들 확인
        for to in range(V):
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))

    print(f'최소 비용 : {sum_weight}')
V, E = map(int, input().split())

graph = [[0] * V for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())

    # 가중치(비용) 저장
    graph[s][e] = w
    graph[e][s] = w
    
    prim(0)