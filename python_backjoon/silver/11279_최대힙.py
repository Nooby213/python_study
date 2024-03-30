import sys
input = sys.stdin.readline
from heapq import heappush, heappop
# 연산 개수 N, 1 ≤ N ≤ 100,000
N = int(input())
heapq = []
for _ in range(N):
    command = int(input())
    if command == 0:
        if heapq:
            print(-heappop(heapq))
        else:
            print(0)
    else:
        heappush(heapq, -command)
